import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '2dabfc697117dbe9497174c9f1f40809'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '28624'

def test_status_code():
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_trainer_name_in_response():
    response = requests.get(f"{URL}/trainers", params={"trainer_id": TRAINER_ID})
    response_data = response.json()
    print(response_data)