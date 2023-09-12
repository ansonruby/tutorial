

import json
import requests
from requests.auth import HTTPDigestAuth

"""
headers = {'Authorization': 'abcde12345'}
print(requests.get('https://httpbin.org/basic-auth/user/pass', headers=headers))


print ('hola')


url = "http://192.168.1.70/ISAPI/AccessControl/RemoteControl/door/1"

username = "admin"
password = "Abcd1234"

response = requests.put(url, auth=(username, password))

print(response.status_code)
#print(response.json())

#--------------------------------------
 
URL = "http://192.168.1.70/ISAPI/AccessControl/RemoteControl/door/1"
 
headers = {
           "accept": "application/json",
           "Content-Type": "application/json"
          }
 
params =  {
          "user": "admin",
          "password": "Abcd1234"
          }
 
resp = requests.put(URL, headers = headers ,data=json.dumps(params),verify=False)
#tk = json.loads(resp.text)['token']
print(resp.text)

"""


url = 'http://192.168.1.70/ISAPI/AccessControl/RemoteControl/door/1'
xml = """<?xml version = "1.0" encoding = "UTF-8"?>
        <RemoteControlDoor>
            <cmd >open</cmd>
        </RemoteControlDoor>
"""
headers = {'Content-Type': 'application/xml'}

#r = requests.put(url, data=xml, headers=headers)





#headers = DEFAULT_HEADERS
headers['Content-Length'] = str(len(xml))
headers['Host'] = 'ggg'
response = requests.put(url, auth=HTTPDigestAuth('admin', 'Abcd1234'), data=xml, headers=headers)
print(response.text)


"""
# -------------  funciona
url = 'http://192.168.1.70/ISAPI/System/capabilities'
response = requests.get(url, auth=HTTPDigestAuth('admin', 'Abcd1234'))
print ("no esta funcionando")
print(response.text)
"""