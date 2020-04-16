from datetime import datetime

def gettime ():
    print(datetime.now())

def initial(name):
    initial = name[0:1].upper()
    return initial

firstname = input("Please enter your first name : ")
lastname = input("Please enter your last name : ")

print("your initial name is " + initial(firstname) + initial(lastname) )
print("today is ")
gettime()