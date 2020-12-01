from mycroft import MycroftSkill

import RPi.GPIO as GPIO


class WakeWordLedGpio(MycroftSkill):
    def __init__(self):
        super(AlarmSkill, self).__init__()
        self.configured = False

    def _setup(self):
        self.pin_mode = self.settings.get('pin_mode', 'board').upper()
        self.pin_number = self.settings.get('pin_number')

        if not self.pin_number:
            self.speak_dialog('error.setup', data={"field": "pin"})
            self.log.warning('PIN number is not configured')
        else:
            self.configured = True
            self.log.info('LED PIN number set to {}'.format(self.pin_number))

        self.log.info('PIN mode set to {}'.format(self.pin_mode))

    def initialize(self):
        self.settings_change_callback = self.on_websettings_changed
        self.on_websettings_changed()

    def on_websettings_changed(self):
        self._setup()
        self._run()

    def _run(self):
        if self.configured:
            try:
                # Setup GPIO
                GPIO.setmode(eval('GPIO.{}'.format(self.pin_mode)))
                GPIO.setwarnings(False)
                GPIO.setup(self.pin_number, GPIO.OUT)

                # Catch event
                self.add_event('recognizer_loop:record_begin',
                               self._handle_listener_started)
                self.add_event('recognizer_loop:record_end',
                               self._handle_listener_ended)
            except:
                self.log.error('Cannot initialize GPIO - skill will not load')
                self.speak_dialog('error.initialize')

    def _handle_listener_started(self, message):
        GPIO.output(self.pin_number, GPIO.HIGH)

    def _handle_listener_ended(self, message):
        GPIO.output(self.pin_number, GPIO.LOW)


def create_skill():
    return WakeWordLedGpio()
