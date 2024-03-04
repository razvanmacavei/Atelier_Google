# import requests
#
# url = "http://localhost:8000/api/location/"
#
# payload = {}
# headers = {}
#
# response = requests.request("GET", url, headers=headers, data=payload)
#
# print(response.text)

# import requests
# import json
#
# url = "http://localhost:8000/api/location/"
#
# payload = json.dumps({
#   "city": "Timisoara2",
#   "country": "Romania"
# })
# headers = {
#   'Content-Type': 'application/json'
# }
#
# response = requests.request("POST", url, headers=headers, data=payload)
#
# print(response.json())

#
# import requests
# import json
#
# url = "http://localhost:8000/api/location/16/"
#
# payload = json.dumps({
#   "city": "Cluj",
#   "country": "Romania"
# })
# headers = {
#   'Content-Type': 'application/json'
# }
#
# response = requests.request("PUT", url, headers=headers, data=payload)
#
# print(response.text)


import requests
import json

url = "http://localhost:8000/api/location/16/"

payload = json.dumps({
  "city": "Cluj",
  "country": "Romania"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)

