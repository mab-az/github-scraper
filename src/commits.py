import json
import requests
from src.helpme import save_json, extract_data

class Commit():
    
    def __init__(self , username , project_id , sha):
        self.username = username
        self.project_id = project_id
        self.sha = sha

    def get_commit_stats(self):
        CommitURL = 'https://api.github.com/repos/{}/{}/commits/{}'.format(self.username, self.project_id, self.sha)
        CommitDataFromGithub = requests.get(CommitURL).json()
        CommitDataFromGithub = extract_data(['commit'], CommitDataFromGithub)
        DataNeeded = [
            'committer',
            'commit',
            'message',
        ]

        CommitData = extract_data(DataNeeded, CommitDataFromGithub)
        save_json('output_of_commit', CommitData)
    


project = Commit('user' , 'repo' , 'commit-id') 
project.get_commit_stats()
        
        