import requests

r = requests.get('https://api.github.com')
response = r.headers
print("Headers: ")
print(response)

print("\nInfo: ")
print("Date: ", r.headers['Date'])
print("Server: ", r.headers['Server'])
print("Content-type: ", r.headers['Content-Type'])



