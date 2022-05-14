import requests

payload = {'key1':'value1', 'key2': 'value2'}
print("Parameters: ", payload)

r = requests.get('https://httpbin.org/get', params = payload)
print("Printing the URL to verify: ")
print(r.url)

print("\nPassing a list as a value: ")
payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
print("Parameters: ", payload)

r = requests.get('https://httpbin.org/get', params = payload)
print("Print the URL to verify: ")
print(r.url)