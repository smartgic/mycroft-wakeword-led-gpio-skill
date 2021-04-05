"""Wake word LED GPIO entrypoint skill
"""
from mycroft import MycroftSkill
import RPi.GPIO as GPIO

__author__ = 'smartgic'


class WakeWordLedGpio(MycroftSkill):
    """This is the place where all the magic happens for the
    wake word LED GPIO skill.
    """

    def __init__(self):
        MycroftSkill.__init__(self)

        # Initialize variables with empty or None values.
        self.configured = False

    def _setup(self):
        """Provision initialized variables and retrieve configuration
        from home.mycroft.ai.
        """
        # By default the GPIO module will be configured with BCM.
        # https://raspberrypi.stackexchange.com/a/12967
        self.pin_mode = self.settings.get('pin_mode', 'bcm').upper()
        self.pin_number = self.settings.get('pin_number')

        # Make sure the requirements are fulfill.
        if not self.pin_number:
            self.speak_dialog('error.setup', data={"field": "pin"})
            self.log.warning('PIN number is not configured')
        else:
            self.configured = True
            self.log.info('LED PIN number set to {}'.format(self.pin_number))

        self.log.info('PIN mode set to {}'.format(self.pin_mode))

    # See https://bit.ly/37pwxIC (Mycroft documentation about skill lifecycle)
    def initialize(self):
        """The initialize method is called after the Skill is fully
        constructed and registered with the system. It is used to perform
        any final setup for the Skill including accessing Skill settings.
        https://tinyurl.com/4pevkdhj
        """
        self.settings_change_callback = self.on_websettings_changed
        self.on_websettings_changed()

    def on_websettings_changed(self):
        """Each Mycroft device will check for updates to a users settings
        regularly, and write these to the Skills settings.json.
        https://tinyurl.com/f2bkymw
        """
        self._setup()
        self._run()

    def _run(self):
        """Based on event, functions will be called to send different
        notifications.
        """
        if self.configured:
            try:
                # Setup GPIO
                GPIO.setmode(eval('GPIO.{}'.format(self.pin_mode)))
                GPIO.setwarnings(False)
                GPIO.setup(self.pin_number, GPIO.OUT)

                # Catch events
                self.add_event('recognizer_loop:record_begin',
                               self._handle_listener_started)
                self.add_event('recognizer_loop:record_end',
                               self._handle_listener_ended)
            except Exception:
                self.log.error('Cannot initialize GPIO - skill will not load')
                self.speak_dialog('error.initialize')

    def _handle_listener_started(self, message):
        """Handle the record_begin event detection and turn the LED on.
        """
        GPIO.output(self.pin_number, GPIO.HIGH)

    # Turn off LED
    def _handle_listener_ended(self, message):
        """Handle the record_end event detection and turn the LED off.
        """
        GPIO.output(self.pin_number, GPIO.LOW)


def create_skill():
    """Main function to register the skill
    """
    return WakeWordLedGpio()
