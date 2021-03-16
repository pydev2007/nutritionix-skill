from mycroft import MycroftSkill, intent_file_handler


class Nutritionix(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('nutritionix.intent')
    def handle_nutritionix(self, message):
        self.speak_dialog('nutritionix')


def create_skill():
    return Nutritionix()

