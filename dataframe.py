import pandas as pd
import numpy as np

df2 = {'name': ['jay', 'mich', 'step', 'sana'],
'email': ["jayp@gmail.com", "mich@gmail.com", "stephanie@gmail.com", "sanana@gmail.com"],
'password': ["hellohacks","michw0821","hello","hacks"],
    }
df_marks = pd.DataFrame(df2)
print('Original DataFrame\n------------------')
#print(df_marks)
#df_marks.to_csv("dataFrame.csv")


def addUser(un,em,pw):
    new_row = {'name': un, 'email' : em , "password" : pw}

    finaldf = df_marks.append(new_row, ignore_index=True)
    #print(finaldf)
    finaldf.to_csv("dataFrame.csv")

#addUser("benny","sana@gmail.com","sananananana")
#def getUserInfo(un):
#    for i in range(len(df2)):
#        print(df2.loc[i, "name"], df.loc[i, "email"])

#getUserInfo('jay')

#def csvtojson():
#    csvcheck = pd.read_csv('dataframe.csv')
#    csvcheck.to_json(r'dataBase.json')

#csvtojson()