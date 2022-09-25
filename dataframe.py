import pandas as pd
import numpy as np

df2 = {'name': ['jay', 'mich', 'step', 'sana'],
'email': ["jayp", "mich@gmail.com", "stephanie@gmail.com", "sanana@gmail.com"],
'password': ["hi","yo","halla","hacks"],
    }
df_marks = pd.DataFrame(df2)
print('Original DataFrame\n------------------')
print(df_marks)
#df_marks.to_csv("dataFrame.csv")


def addUser(un,em,pw):
    new_row = {'name': un, 'email' : em , "password" : pw}

    finaldf = df_marks.append(new_row, ignore_index=True)
    #print(finaldf)
    finaldf.to_csv("dataFrame.csv")

addUser("benny","sana@gmail.com","sananananana")

def getUserInfo(un):
    df_marks.dropna(inplace = True)
    start = 0
    df_marks["Indexes"]= df_marks["name"].str.find(un, start)
    print(df_marks["name"].where(df2["Indexes"] > -1))
    print(df_marks["e-mail"].where(df2["Indexes"] > -1))
    print(df_marks["password"].where(df2["Indexes"] > -1))
    return df_marks

#print(df2)
print(getUserInfo('jay'))




#entry = [df2,"michelle","michelle@gmail.com", "mcpassword"]
#pd.concat(entry)

#import csv
#import json
 
#def make_json(csvFilePath, jsonFilePath):
#    data = {}
#    with open(csvFilePath, encoding='utf-8') as csvf:
#       csvReader = csv.DictReader(csvf)
#        for rows in csvReader:
#            key = rows['No']
#            data[key] = rows

#    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
#        jsonf.write(json.dumps(data, indent=4))

#csvFilePath = 'dataFrame.csv'
#jsonFilePath = 'dataBase.json'
#make_json("dataFrame.csv", "dataBase.json")