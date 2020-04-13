x = 100
y = int(input("Please enter the number to dived 100 : "))

try:
    print(x/y)
except ZeroDivisionError as o:
    print("Youre not allowed to divide number with zero")
else:
    print("Something else happening except zero")
finally:
    print("Yeay this handling stuff is finished")
