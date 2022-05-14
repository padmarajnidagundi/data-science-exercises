import requests

response = requests.get('https://rigaux.org', verify=False)
print(response)

response1 = requests.get('https://google.com')
print(response1)

response1 = requests.get('https://google.com', verify=True)
print(response1)

