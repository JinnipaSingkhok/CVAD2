import pandas as pd
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 22]
})
df.to_csv("OIIA.csv",index=False)
df = pd.read_csv("OIIA.csv")
print(df)
