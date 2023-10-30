import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]}
df = pd.DataFrame(data)

filtered_df = df[df['Age'] > 28]
print(filtered_df)
