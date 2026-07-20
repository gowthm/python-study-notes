import requests

try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts",
        timeout=5
    )
    response.raise_for_status()
    data = response.json()
    print(data)
except requests.Timeout:
    print("Request Timeout")
except requests.HTTPError as e:
    print(e)
except requests.RequestException as e:
    print(e)