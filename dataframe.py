
import pandas as pd
data={"sr.no":[1,2],"name":["devidas","prethamesh"],"age":[22,23]}
df=pd.DataFrame(data)
print(df)
r=df[df["age"]>22]
print(r)
 
