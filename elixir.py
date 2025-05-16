import pandas as pd
import requests

url = "https://wizard-world-api.herokuapp.com/Elixirs"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print('Success!')
    data = response.json()
else:
    print(f"Error: {response.status_code}")
    data = []

# Create DataFrame from the elixirs
df = pd.DataFrame(data)

print(df.head())
