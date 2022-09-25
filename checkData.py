from ast import Str
from xmlrpc.client import boolean


def add_user(us,em,pw):
    check = "[USER: " + us 

    with open('database.txt') as f:
        lines = f.readlines()
    if check not in lines:
        write_user(us,em,pw)
def add_course(us, en, pw, cn):
    check = "[USER: " + us 


    with open('database.txt') as f:
        lines = f.readlines()
    pos = lines.index(check)
    lines = lines[:pos + 2 + en.length() + pw.length()] + str(cn) + lines[pos + 2 + en.length() + pw.length():]
    lines.find(check)



def write_user(username, email, password):
    f = open('database.txt', 'a')
    f.write("\n" + "[USER: " + str(username) + "," + str(email) + "," + str(password) + "]")
    f.close()
    

def write_course(courseName):
    f = open('database.txt', 'a')

    f.write(str(courseName))
    f.close()

def write_module(moduleName, finished):
    f = open('database.txt', 'a')
    f.write("["+ str(moduleName) + "," + Str(finished) + "]")
    f.close()
def clear():
    f = open('database.txt', 'w')
    f.write("")
    f.close()


add_user("jay","jay", "jay")
add_course("jay", "jay", "gay", "CPSC110" )