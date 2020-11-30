from mycroft import MycroftSkill
from mycroft.messagebus.message import Message

import RPi.GPIO as GPIO


class WakeWordLedGpio(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def on_settings_changed(self):
        self.pin_mode = self.settings.get('pin_mode', 'board').upper()
        self.pin_number = self.settings.get('pin_number', 10)
        self.log.info('PIN mode set to {}'.format(self.pin_mode))
        self.log.info('LED PIN number set to {}'.format(self.pin_number))

    def initialize(self):
        self.settings_change_callback = self.on_settings_changed
        self.on_settings_changed()

        try:
            # Setup GPIO
            GPIO.setmode(eval('GPIO.{}'.format(self.pin_mode)))
            GPIO.setwarnings(False)
            GPIO.setup(self.pin_number, GPIO.OUT)

            # Catch event
            self.add_event('recognizer_loop:record_begin',
                           self.handle_listener_started)
            self.add_event('recognizer_loop:record_end',
                           self.handle_listener_ended)
        except Exception:
            GPIO.cleanup()
            self.log.error('Cannot initialize GPIO - skill will not load')
            self.speak_dialog('error.initialize')

    def handle_listener_started(self, message):
        GPIO.output(self.pin_number, GPIO.LOW)

    def handle_listener_ended(self, message):
        GPIO.output(self.pin_number, GPIO.HIGH)


def create_skill():
    return WakeWordLedGpio()
