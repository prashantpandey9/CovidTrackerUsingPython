import requests

import json

def country():
    api="https://corona.lmao.ninja/v2/countries#"

    s=(requests.get(api)).text

    data=json.loads(s)
    for j in data:
        print(j['country'],j['cases'])
    
country()
