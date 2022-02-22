import json
from bs4 import BeautifulSoup as bs
import os


def parse_github_people_list():
    """ Use the downloaded page to parse GitHub Organisation members logins """
    users = []

    for file in os.listdir('data'):
        if '.html' in file:
            file_path = f"data/{file}"
            print(file_path)
        
            with open(file_path, 'r') as response:
                soup = bs(response, 'html.parser')
                
                for link in soup.find_all(class_="d-inline-block"):
                    
                    path = link.get('href')

                    if path:
                        user = path.split('/')[-1]
                        users.append(user)


    unique_users = set(users)

    with open('results/users_list.json', 'w') as f:
        json.dump(unique_users, f, indent= True)


if __name__ == "__main__":
   
    parse_github_people_list()
