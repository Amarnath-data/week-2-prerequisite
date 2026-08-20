import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

response.raise_for_status()

data = response.json()

df = pd.DataFrame(data)

print(df)

df.to_csv("API_Data_Extraction.csv", index=False)