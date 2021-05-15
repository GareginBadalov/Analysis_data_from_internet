import requests
import json


repos = requests.get('https://api.github.com/users/GareginBadalov/repos').json()
with open('repos_for_user.json', 'w') as fp:
    json.dump(repos, fp, indent=4)
