import requests
import pytest

url_trainers=''

def test_check_status_code():
    response = requests.get(url_trainers)
    assert response.status_code==200

def test_check_trainer_name():
    response = requests.get(url_trainers,
                           params={'trainer_id': 4256})
    assert response.json()['trainer_name']=='Pokeshka'

@pytest.mark.parametrize('key, value', [('trainer_name','Pokeshka'),('city','Kazan')])
def test_check(key,value):
    response = requests.get(url_trainers,
                           params={'trainer_id': 4256})
    assert response.json()[key]==value