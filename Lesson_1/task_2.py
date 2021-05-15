import requests
import json
import cnf

user = requests.get('https://badalovgm.testrail.io/index.php?/api/v2/get_user/1', auth=(cnf.login, cnf.password)).json()

with open('api_auth.json', 'w', encoding='UTF-8') as fp:
    json.dump(user, fp,  ensure_ascii=False, indent=4)
