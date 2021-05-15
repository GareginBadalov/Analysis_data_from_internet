import requests
import json


jokes_dict = {'jokes': []}
for num_of_jokes in range(100):
    response = requests.get('https://api.kanye.rest/').json()
    jokes_dict['jokes'].append({'№': num_of_jokes + 1, 'joke': response['quote']})

with open('jokes.json', 'w', encoding='Utf-8') as f:
    json.dump(jokes_dict, f, indent=4, ensure_ascii=False)
