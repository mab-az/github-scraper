import json
import requests


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


def users_left_to_scape():
    with open('results/az_contributors.json', 'r') as f:
        users_p = json.load(f)

    for user in users_p:
        username = user['login']
        with open(f'user_profiles/{username}.json', 'w') as f:
            json.dump(user, f)

    users_present = [x['login'] for x in list(users_p)]

    with open('results/az_users_list.json', 'r') as f:
        users_all = json.load(f)

    diff = [x for x in users_all if x not in users_present]

    print(diff)
    print(len(diff), len(users_all))

    with open(f'results/users_to_add.json', 'w') as f:
            json.dump(diff, f)






if __name__ == "__main__":
    # """ Takes a list of Organisation members and scrapers each individual's profile """
    # contributors = []

    # with open('results/az_users_list.json', 'r') as f:
    #     users = json.load(f)

    # for username in users:
    #     print(f"Username: {username}")
    #     user_stats = User(username).get_user_stats()

    #     # print(f"User stats: {len(user_stats)}")

    #     contributors.append({"author": user_stats})

    # with open('results/contributors.json', 'w') as f:
    #     json.dump(contributors, f)


    
    users_left_to_scape()
    