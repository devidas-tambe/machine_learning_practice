import pandas as pd
data={
    "name":["sagar", "Hitesh", "Rushi", "prathamesh"],
    "age":[20,30,None, 30],
    "salary":[2000,None, 1000, None]
}

df=pd.DataFrame(data)
print(df)

print(df.isnull().sum())

print(df.dropna())

df["age"]=df["age"].fillna(df["age"].mean(), inplace=True)
df["salary"]=df["salary"].fillna(df["salary"].mean(), inplace=True)
print(df)

print(df.isnull().mean()*100)