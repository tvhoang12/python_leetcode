import pandas as pd

data = {'Name': ['John', 'Emma', 'Peter', 'David', 'Sophie'],
        'Age': [27, 21, 24, 30, 29],
        'Gender': ['Male', 'Female', 'Male', 'Male', 'Female'],
        'City': ['New York', 'London', 'Paris', 'Tokyo', 'Rio de Janeiro']}
df = pd.DataFrame(data)
df2 = pd.DataFrame(df[df['Age'] == 27])
df2 = df2.drop(['Age'], axis=1)
print(df2)