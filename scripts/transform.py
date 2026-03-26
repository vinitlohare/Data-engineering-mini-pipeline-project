import pandas as pd 
df = pd.read_csv('data/raw_data.csv')
print(df)
print("Raw data:")
df['annual_salary']=df['salary'] * 12
print("Transformed data")
print(df)
df.to_csv('data/processed_data.csv',index=False)
print("Processed data saved successfully!")