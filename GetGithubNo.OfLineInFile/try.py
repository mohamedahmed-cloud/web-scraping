import requests

# Make an HTTP GET request to a JSON API
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")

# Convert the JSON response into a Python object
data = response.json()

# Print the resulting Python object
print(type(response))