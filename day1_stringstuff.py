#first = "fahri"
#last = "novald"
first = input("Please input your fucking name : ")
last = input("and your last name too, lol : ")
print("Hello, " + first.capitalize() + " " + last.capitalize())


# formatting string stuff

output = "Hello, {1} {0}".format(first, last)

print(output)

output = f"hello, {first.capitalize()} {last.capitalize()}"

print(output)