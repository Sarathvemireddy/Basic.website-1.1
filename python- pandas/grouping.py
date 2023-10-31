import pandas as pd

data = {'Category': ['A', 'B', 'A', 'B'],
        'Value': [10, 15, 20, 25]}
df = pd.DataFrame(data)

grouped = df.groupby('Category')['Value'].sum()
print(grouped)
