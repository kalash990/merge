import requests
import json
url = "https://dev.azure.com/KalashAzure/New Game/_apis/wit/workitems/$Epic?api-version=6.0"

payload = json.dumps([
  {
    "op": "add",
    "path": "/fields/System.Title",
    "value": "New Task"
  }
])
headers = {
  'Authorization': 'Basic OmZqdDRlZnJqcHlkZGRzcG1uamNqY3gzaXM1Ym01b3ZibGM1djVxZTY0cTJiN21iaHZ2ZGE=',
  'Cookie': 'VstsSession=%7B%22PersistentSessionId%22%3A%2262b591c1-a7c3-410c-916c-5b2404d5415b%22%2C%22PendingAuthenticationSessionId%22%3A%2200000000-0000-0000-0000-000000000000%22%2C%22CurrentAuthenticationSessionId%22%3A%2200000000-0000-0000-0000-000000000000%22%2C%22SignInState%22%3A%7B%7D%7D',
  'Content-Type': 'application/json-patch+json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.json)
