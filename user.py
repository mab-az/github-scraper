import json
import requests
from helpme import extract_data, save_json


class User():

    def __init__(self, Username):
        self.Username = Username
        self.UserURL = 'https://api.github.com/users/{}'.format(self.Username)        

    def get_user_stats(self):
        UserDataFromGithub = requests.get(self.UserURL).json()
        DataNeeded = [
            'login', 'id', 'node_id', 'avatar_url', 'gravatar_id', 'url', 
            'html_url', 'followers_url', 'following_url', 'gists_url', 
            'starred_url', 'subscriptions_url', 'organizations_url', 
            'repos_url', 'events_url', 'received_events_url', 'type', 
            'site_admin'
            ]
        self.UserData = extract_data(DataNeeded, UserDataFromGithub)
                
        save_json('output_of_User' , self.UserData)

        return json.dumps(self.UserData, indent= True)


avikant = User('mab-az')
data = avikant.get_user_stats()
print(data)