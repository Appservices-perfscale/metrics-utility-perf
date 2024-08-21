import requests
import json
from base64 import b64encode


def basic_auth(username, password):
    token = b64encode(f"{username}:{password}".encode('utf-8')).decode("ascii")
    return f'Basic {token}'

def creating_hosts(payload_list, url="https://44.203.184.194/api/controller/v2/bulk/host_create/"):
    
    username = "admin"
    password = "Admin!Password!Gw"
    
    print(basic_auth(username, password))

    headers = {
        "Content-Type": "application/json",
        "Authorization": basic_auth(username, password)
    }
    

    payload = json.dumps(
        {
            "inventory": 3, "hosts": payload_list
        }
    )

    response = requests.request("POST", 
        url=url, headers=headers, data=payload, verify=False
    )
    print(response.text)
    return response

def creating_payload(number_hosts):
    
    payload_list = list()
    
    for numb in range(0,number_hosts):
        
        payload_list.append({"name": f"example{numb}.com", "variables": "ansible_connection: local"})
        
    return payload_list
    
    
payload_ = creating_payload(3000) #select # hosts to create

creating_hosts(payload_)