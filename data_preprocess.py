import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('building_inventory.csv', na_values = {'Year Acquired':0,'Year Constructed':0})
# df['Year Acquired'] = pd.to_datetime(df['Year Acquired'] )
# df['Year Constructed']= pd.to_datetime(df['Year Constructed'])
df.columns
df = df.dropna(subset=['Year Acquired', 'Year Constructed'])
df.to_csv('bd_data.csv',encoding='utf-8-sig', index=False)
df
df['']
plt.scatter(df['Year Acquired'], df['Year Constructed'])

df['Year Acquired'].dtype


