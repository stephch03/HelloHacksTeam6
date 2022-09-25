from ast import Str
from xmlrpc.client import boolean


def add_user(us,em,pw):
    check = "(USER: " + us 

    with open('database.txt') as f:
        lines = f.readlines()
    if check not in lines:
        write_user(us,em,pw)

def add_course(us, en, pw, cn):
    check = "[USER: " + us 
    courseCheck ="(COURSE: " + cn
    print(courseCheck)
    with open('database.txt') as f:
        lines = f.readlines()
        length = len(lines)

        for i in range(length):

            if check in lines[i]:
                if courseCheck not in lines[i]:
                    end = lines[i].index("]")
                    lines[i] =  lines[i][:end] + "(" + "COURSE: " + cn + ")" + "]"

        f = open('database.txt', 'w')
        #clear()
        for i in range(length):
            f.write(lines[i] + "\n")
        f.close()
def add_module(us, cn, mn):
    check = "[USER: " + us 
    courseCheck ="(COURSE: " + cn
    with open('database.txt') as f:
        lines = f.readlines()
        length = len(lines)

        for i in range(length):

            if check in lines[i]:
                if courseCheck in lines[i]:
                    cnl = len(courseCheck)
                    cl = len(cn)

                    cc = lines[i].index(courseCheck)

                    lines[i] =  lines[i][:cc + cnl ]+ " ,"  + mn + lines[i][cc + cnl :] 
                    print (lines[i])
        clear()
        f = open('database.txt', 'w')
        
        for i in range(length):
            f.write(lines[i] )
        f.close()


def write_user(username, email, password):
    f = open('database.txt', 'a')
    
    f.write('\n' + "[USER: " + str(username) + "," + str(email) + "," + str(password) + "]")
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
#clear()
#add_user("emily","jay", "jay")
#add_course("jay", "jay", "gay", "CPSC110" )
add_module("jay", "CPSC110", "HTDF")