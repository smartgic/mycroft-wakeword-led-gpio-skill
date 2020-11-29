from mycroft import MycroftSkill, intent_file_handler


class WakeWordLedGpio(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('gpio.led.word.wake.intent')
    def handle_gpio_led_word_wake(self, message):
        self.speak_dialog('gpio.led.word.wake')


def create_skill():
    return WakeWordLedGpio()

