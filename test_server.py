import requests

print(
  requests.post(
    "http://0.0.0.0:10000/",
    json = {
      "query": "What is Meta's new product Thread?"
    }
  ).json()
)