from mycroft import MycroftSkill, intent_file_handler


class WakeWordLedGpio(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.pin_mode = self.settings.get('pin_mode')
        self.pin_number = self.settings.get('pin_number')

    def initialize(self):
        try:
            GPIO.setmode(self.pin_mode)
            GPIO.setwarnings(False)
            GPIO.setup(self.pin_number, GPIO.OUT)
        except GPIO.error:
            self.log.warning("Cannot initialize GPIO - skill will not load")
            self.speak_dialog("error.initialize")
        finally:
            self.add_event('recognizer_loop:record_begin',
                           self.handle_listener_started)
            self.add_event('recognizer_loop:record_end',
                           self.handle_listener_ended)

    def handle_listener_started(self, message):
        GPIO.output(self.pin_number, GPIO.HIGH)

    def handle_listener_ended(self, message):
        GPIO.output(self.pin_number, GPIO.LOW)


def create_skill():
    return WakeWordLedGpio()
