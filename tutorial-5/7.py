import pandas as pd
data_dict = {
    'Name': ['Linus Torvalds', 'Tim Berners-Lee', 'Guido van Rossum'],
    'Country': ['Finland', 'England', 'Netherlands'],
    'Contribution': ['Linux Kernel', 'World Wide Web', 'Python'],
    'Year': [1991, 1990, 1991]
}

df = pd.DataFrame(data_dict)
df.insert(0, 'SN', range(1, len(df) + 1))
print(df)