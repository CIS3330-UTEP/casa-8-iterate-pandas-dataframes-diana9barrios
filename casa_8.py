import pandas as pd 
df = pd.read_csv('big-mac-full-index.csv')
df.head()

#Method 4: Using iterrows() method
for i,r in df.iterrows():
    print(r['date']), r['name']


#Method 6: Using apply() method
print(df.apply(lambda row: row['name'], axis = 1))