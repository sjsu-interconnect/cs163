import requests
import json

url = "https://pchecker-image-611571974386.us-west2.run.app/check_prime"

payload = {"number" : 13}

response = requests.post(url, json.dumps(payload))

print(response.text)

# Or you can use Postman.
# https://www.postman.com/