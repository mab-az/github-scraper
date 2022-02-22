import json
import requests
from helpme import save_json, extract_data, group_with_same_key


class Repo():
    def __init__(self, username, project_name):
        self.username = username
        self.project_name = project_name

    def get_repo_stats(self):
        RepoURL = 'https://api.github.com/repos/{}/{}'.format(
            self.username, self.project_name)
        RepoDataFromGithub = requests.get(RepoURL).json()

        DataNeeded = [
            'name',
            'html_url',
            'description',
            'forks',
            'open_issues',
            'language',
            'git_url',
        ]

repo = Repo('mab-az', 'repo-name')
data = repo.get_repo_stats()
repo.get_sha_values()
# print(data)
