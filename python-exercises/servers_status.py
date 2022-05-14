import requests

res = requests.get('https://amazon.com')
print("Amazon response: ")
print(res)

res = requests.get('https://google.com')
print("Google response: ")
print(res)

