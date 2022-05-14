import requests

res = requests.get('https://google.com')
print("Google server response: ")
print(res)

print("\n Content of the URL: ")
print(res.content)