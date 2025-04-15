import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '2dabfc697117dbe9497174c9f1f40809'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '28624'
body_poks = {
    "name": "Бульбазавр",
    "photo_id": 12
}
body_name = {
    "pokemon_id": "290394",
    "name": "djdj",
    "photo_id": 2
}
body_pokeboll = {
    "pokemon_id": "290399"
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_poks)
print(response.text)

response_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_name)
print(response_name.text)

response_pokeboll = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeboll)
print(response_pokeboll.text)