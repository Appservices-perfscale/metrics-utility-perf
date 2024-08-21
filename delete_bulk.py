import requests
import json
from base64 import b64encode


def basic_auth(username, password):
    token = b64encode(f"{username}:{password}".encode('utf-8')).decode("ascii")
    return f'Basic {token}'

def getting_hosts(url="https://44.203.184.194/api/controller/v2/inventories/3/hosts/"):
    
    username = "admin"
    password = "Admin!Password!Gw"
    
    print(basic_auth(username, password))

    headers = {
        "Content-Type": "application/json",
        "Authorization": basic_auth(username, password)
    }

    response = requests.request("GET", 
        url=url, headers=headers, verify=False
    )
    return response.json()


def fetching_only_hosts(full_response, number_hosts):
    
    first_number = full_response['results'][0]['id']
    list_number = list()
    
    for n in range(first_number, first_number + number_hosts):
        list_number.append(n)
        
    return list_number
    
def deleting_hosts(list_ids, url="https://44.203.184.194/api/controller/v2/bulk/host_delete/"):
    
    username = "admin"
    password = "Admin!Password!Gw"
    
    print(basic_auth(username, password))

    headers = {
        "Content-Type": "application/json",
        "Authorization": basic_auth(username, password)
    }
    
    payload = json.dumps(
        {
            "hosts": list_ids
        }
    )

    response = requests.request("POST", 
        url=url, headers=headers, data=payload, verify=False
    )
    print(response.text)
    return response
    

f_resp = getting_hosts()
id_hosts = fetching_only_hosts(f_resp, 3000)

deleting_hosts(id_hosts)




    
    