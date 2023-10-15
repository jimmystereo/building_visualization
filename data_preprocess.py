import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('building_inventory.csv', na_values = {'Year Acquired':0,'Year Constructed':0})
# df['Year Acquired'] = df['Year Acquired'].apply(lambda x: str(x))
# df['Year Constructed']= df['Year Constructed'].apply(lambda x: str(x))
df.columns
df = df.dropna(subset=['Year Acquired', 'Year Constructed'])
df
df.to_json ('bd_data.json')

df.to_csv('bd_data.csv',encoding='utf-8-sig', index=False)
df
df['']
plt.scatter(df['Year Acquired'], df['Year Constructed'])


df['Year Acquired'].min()

df['Year Acquired'].max()
df['Year Constructed'].min()

df['Year Constructed'].max()


df2 = pd.read_csv("bd_data.csv")
df2