import requests
import json

def req(a, b):
    url = "https://faas-fra1-afec6ce7.doserverless.co/api/v1/web/fn-1f1056ff-de8e-4509-9811-27a68419f504/default/add"

    payload = {"a": a, "b": b}  # json
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, json=payload)

    if 'result' not in json.loads(response.text):
        raise Exception('No hay result')
    # print('STATUS:  ', response.status_code)
    # print('RESPONSE:', response.text)

    print(json.loads(response.text)['result'])
    return int(json.loads(response.text)['result'])
# assert response.status_code == 200
# assert response.headers['Content-type'] == 'application/json'

assert req(1, 3) == 4
