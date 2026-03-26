import pandas as pd 
df = pd.read_csv('data/raw_data.csv')
print("Raw data:")
print(df)

df['salary']=df['salary'] * 1.1
df.to_csv('data/processed_data.csv',index=False)
print("Processed data saved successfully!")