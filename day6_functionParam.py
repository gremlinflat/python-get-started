def initial (name, Forceupper = True):
    if Forceupper:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

firstname = input("Please enter your first name : ")
lastname = input("Please enter your last name : ")
email = input("Please enter your email : ")
print("your initial name is " + initial(firstname, True) + initial(lastname, False) )
print("your email address is " + initial(email, False))