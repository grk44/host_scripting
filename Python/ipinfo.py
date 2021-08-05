#https://ipinfo.io/8.8.8.8/json


import json, requests,logging as log
log.basicConfig(level=log.INFO, format=' %(asctime)s -%(levelname)s -  %(message)s')

ip=input('Enter IP Address: ')
log.debug('IP: ' + ip)
url='https://ipinfo.io/%s/json' % (ip)
log.debug('URL: ' + url)

response=requests.get(url)
response.raise_for_status()

log.debug('JSON RESPONSE: ' + response.text)

i = json.loads(response.text)
log.debug(i)

print('IP Address information for ' + ip)
print('HostName: ' + i['hostname'])
print('City: ' + i['city'])
print('Region: ' + i['region'])
print('Location: ' + i['loc'])

