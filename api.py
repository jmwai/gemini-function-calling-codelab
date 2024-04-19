import requests
url = "https://api.frankfurter.app/latest"
response = requests.get(url)
print(response.text)

