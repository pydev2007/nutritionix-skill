from mycroft import MycroftSkill, intent_file_handler
import requests
import json
class Nutritionix(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('nutritionix.intent')
    def handle_nutritionix(self, message):

        api = self.settings.get('ApiKey')

        I = str(message.data.get("item"))

        url = "https://nutritionix-api.p.rapidapi.com/v1_1/search/" + I

        
        querystring = {"fields":"item_name,brand_name,nf_calories,nf_total_fat"}

        headers = {
            'x-rapidapi-key': api ,
            'x-rapidapi-host': "nutritionix-api.p.rapidapi.com"
            }

        response = requests.get(url, headers=headers, params=querystring)
        
        hits = response.json()

        status_code = response.status_code

        food = hits["hits"][0]["fields"]["item_name"]

        fat = hits["hits"][0]["fields"]["nf_total_fat"]

        cals = hits["hits"][0]["fields"]["nf_calories"]

        self.speak(str(food) + " has " + str(cals) + " calories and has a total of " + str(fat) + " grams of fat")
  
def create_skill():
    return Nutritionix()

