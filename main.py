import requests
import names

token = ''
url = ''
url_photo = ''
url_kill = ''
url_add = ''

create=requests.post(url, 
                             headers={'Content-Type': 'application/json', 'trainer_token':token},
                             json={"name": names.get_first_name(),
                                   "photo": url_photo})
print(create.text)

'''
kill=requests.post(url_kill, 
                             headers={'Content-Type': 'application/json', 'trainer_token':token},
                             json={"pokemon_id": "9798"})
print(kill.text)
'''

change_name=requests.put(url, 
                             headers={'Content-Type': 'application/json', 'trainer_token':token},
                             json={"pokemon_id": "9799",
                                   "name": names.get_first_name(),
                                   "photo": url_photo
})
print(change_name.text)

add=requests.post(url_add, 
                             headers={'Content-Type': 'application/json', 'trainer_token':token},
                             json={"pokemon_id": "9799"})
print(add.text)