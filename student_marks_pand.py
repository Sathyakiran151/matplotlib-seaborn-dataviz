'''Load CSV file with student info (name, marks, gender)

Find average marks per subject using df.mean()

Sort students by marks using df.sort_values()
'''
import pandas as pd
a=pd.read_csv("C:\\Users\\HP\\Desktop\\marksheet.csv")
df=pd.DataFrame(a)
df["Total"]=df["Science"]+df["English"]+df["History"]+df["Maths"]
print("THe Total of Student marks:",df)
df["Average"]=df[["Science","English","History","Maths"]].mean(axis=1) 
print("\nTHe Average marks per subject are:",df)
df.sort_values("Total",inplace=True,ascending=False)
print(df)
df.to_csv("C:\\Users\\HP\\Desktop\\marksheet.csv",index=False)

