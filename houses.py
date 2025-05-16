import pandas as pd
import requests

url = "https://wizard-world-api.herokuapp.com/Houses"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print('Success!')
    data = response.json()
else:
    print(f"Error: {response.status_code}")
    data = []

# Create DataFrame
df = pd.DataFrame(data)
# Only keep the important columns to make the table easier to read
df = df[['name', 'founder', 'animal']] 

print(df.head())
