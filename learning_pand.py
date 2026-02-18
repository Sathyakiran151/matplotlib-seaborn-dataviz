import pandas as pd
a=pd.read_csv("C:\\Users\\HP\\Downloads\\BMW.csv")
df=pd.DataFrame(a)
#print(df.head(5))
'''print(df.head(3))
print(df.tail(2))
print(df.describe())
print(df.shape)
print(df[0:12:2])
print(df["model"])
print(df[["year","price"]])
print(df[["year","price"]])[0:122:10]
#for i in df.iterrows():
  #  print(i)'''
#print(df.loc[0])
#print(df.loc[12,"year"])
#print(df.loc[12:14])
#print(df.loc[12:14,"year"])
#print(df.loc[12:14,["year","price"]])
#print(df.loc[12:14,"year":"tax"])

# iloc
#print(df.iloc[0,1]) # first row and next column
#print(df.iloc[0:5,0:3]) # 0 to 4  row annd 0 to 2 column
#print(df.iloc[0:5,0:3])
#print(df.iloc[0:5,2])
#print(df.iloc[[2,4,9]])
#print(df.iloc[:,[1,2,4]])
#print(df.iloc[0:5,[1,2,4]])
#print(df.sort_values("price"))
#print(df.sort_values("price",ascending=False))
#print(df.sort_values(["year","price"]))

#df["new_price"]=df["price"]+1000
#print(df.head(5))

#print(df.duplicated())
#df.drop_duplicates(inplace=True)