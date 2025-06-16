import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'Shachar', 'Dalya'],
    'age': [25, 30, 35, 20, 23],
    'city': ['NYC', 'LA', 'Chicago', 'New York', 'Jerusalem']
}

df = pd.DataFrame(data)
print(df)

# See the first few rows
df.head()

# Get summary stats
df.describe()

# Filter rows
df[df['age'] > 30]

# Add a new column
df['is_adult'] = df['age'] >= 18

# Drop a column
df.drop('city', axis=1)