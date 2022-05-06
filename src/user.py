import json
import requests
import os


def extract_data(DataNeeded, DataFromGithub, ):
    Data = {}
    for (k, v) in DataFromGithub.items():
            if k in DataNeeded:
                Data[k] = v
    return Data


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

        print(UserDataFromGithub)

        self.UserData = extract_data(DataNeeded, UserDataFromGithub)

        return self.UserData


def scrape_all_users():
    """ 
    Takes a list of Organisation members and scrapers each individual's profile 
    BLOCKED: API is blocked after 60 requests in one hour
    """
    contributors = []

    with open('results/az_users_list.json', 'r') as f:
        users = json.load(f)

    for username in users:
        print(f"Username: {username}")
        user_stats = User(username).get_user_stats()
        contributors.append({"author": user_stats})

    with open('results/contributors.json', 'w') as f:
        json.dump(contributors, f)


def create_individual_profiles():
    with open('results/users_to_add.json', 'r') as f:
        users_to_add = json.load(f)

    print(f"All contrinutors: {len(users_to_add)}")
    diff = []

    for username in users_to_add:
        user_stats = User(username).get_user_stats()
        if user_stats:
            print(f"Adding: {username}")
            with open(f'user_profiles/{username}.json', 'w') as f:
                json.dump(user_stats, f)
        else:
            diff.append(username)

    print(f"Newly scraped: {len(users_to_add) - len(diff)}")
    print(f"Missing: {len(diff)}")

    with open(f'results/users_to_add.json', 'w') as f:
            json.dump(diff, f)


def combine_individual_profies(selected_list=None):
    """Creates the contrinutors.json file to be used on the website"""

    contributors = []
    user_list = sorted([x.split(".")[0] for x in set(os.listdir('user_profiles'))])

    for user in user_list:
        with open(f"user_profiles/{user}.json", 'r') as f:
            profile = json.load(f)

        if selected_list:
            if user in selected_list:
                contributors.append({"author": profile})
        else:
            contributors.append({"author": profile})

    print(len(contributors))

    with open('results/contributors_ria.json', 'w') as f:
        json.dump(contributors, f) 



if __name__ == "__main__":
    selected_list = [
 "adam-2-taylor",
 "nithin8702",
 "TatianaSct",
 "homeshsayal",
 "talipucar",
 "jaynanavati-az",
 "AngermannBR",
 "GreetDB",
 "SamuelHLewis",
 "JTT94",
 "eHajiramezaniAZ",
 "mab-az",
 "doglic-az",
 "Hoda-Sharifian",
 "DrClick"
]

    # create_individual_profiles()
    combine_individual_profies(selected_list)
    