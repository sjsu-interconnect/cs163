import requests
import json

url = "http://localhost:8080/predict"

payload = {"feature1" : 1, "feature2" : 2, "feature3" : 3, "feature4" : 4}

response = requests.post(url, json.dumps(payload))

print(response.text)

# Or you can use Postman.
# https://www.postman.com/