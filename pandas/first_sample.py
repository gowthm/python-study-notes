from pathlib import Path
import pandas as pd

json_path = Path(__file__).parent / 'airports.json'
df = pd.read_json(json_path)
df = pd.json_normalize(df['airports'])


print(df.loc[df["city"] == 'London'])
