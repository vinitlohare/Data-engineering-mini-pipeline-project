import pandas as pd 
df = pd.read_csv('data/raw_data.csv')
print(df)
print("Raw data:")
df['salary']=df['salary'] * 0.05
# Add salary category
df['salary_category'] = df['salary'].apply(
    lambda x: 'Low' if x < 3000 else ('Medium' if x <= 5000 else 'High')
)
print("Transformed data")
print(df)
df.to_csv('data/processed_data.csv',index=False)
print("Processed data saved successfully!")