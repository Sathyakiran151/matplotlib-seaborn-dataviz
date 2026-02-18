import pandas as pd
a=pd.read_csv("C:\\Users\\HP\\Desktop\\car_price_prediction_.csv")
df=pd.DataFrame(a)
df["Current Year"]=2025
df["Age of Car"]=df["Current Year"]-df["Year"]
df.loc[df["Condition"]=="New","Decision"]="Buy"
df.loc[df["Condition"]=="Used","Decision"]="Sell"
df.loc[df["Condition"]=="Like New","Decision"]="Hold"
df.loc[df["Price"]<25000,"Price Level"]='Low'
df.loc[(df["Price"]>25000) & (df["Price"]<55000),"Price Level"]='Medium'
df.loc[df["Price"]>55000,"Price Level"]='High'
df.to_csv("C:\\Users\\HP\\Desktop\\car_price_prediction_.csv",index=False)
print(df)