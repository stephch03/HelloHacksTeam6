import pandas as pd
import numpy as np

df2 = pd.DataFrame(
    {
       
        "Name": pd.Categorical(["jay","michelle","stephanie"]),
        "e-mail": pd.Categorical(["jayemail","jayemail","jayemail"]),
        "password": pd.Categorical(["jaypw","jaypw","jaypw"])
        
    })
def addUser(un,em,pw):
    addData = pd.DataFrame(
        {
        "addName": pd.Categorical([un]),
        "adde-mail": pd.Categorical([em]),
        "addpassword": pd.Categorical([pw])
        }
    )


def getUserInfo(un):
    df2.dropna(inplace = True)
    start = 0
    df2["Indexes"]= df2["Name"].str.find(un, start)
    print(df2["Name"].where(df2["Indexes"] > -1))
    print(df2["e-mail"].where(df2["Indexes"] > -1))
    print(df2["password"].where(df2["Indexes"] > -1))
    return df2
addUser("Sana","sana@gmail.com","sananananana")
#print(df2)
#print(getUserInfo('jay'))

df2.to_csv("dataFrame.csv")

#entry = [df2,"michelle","michelle@gmail.com", "mcpassword"]
#pd.concat(entry)