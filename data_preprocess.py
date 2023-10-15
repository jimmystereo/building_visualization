import pandas as pd
df = pd.read_csv('building_inventory.csv', na_values = {'Year Acquired':0,'Year Constructed':0})

df.columns
df = df.dropna(subset=['Year Acquired', 'Year Constructed'])
df.to_csv('bd_data.csv',encoding='utf-8-sig', index=False)
df