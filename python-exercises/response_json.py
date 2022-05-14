import requests

r = requests.get('https://api.github.com')
response = r.json()

print("JSON value: ")
print(response)

print("\nSome keys: ")
print("Current user url: ", response['current_user_url'])
print("Code search url: ", response['code_search_url'])

