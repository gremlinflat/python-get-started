GPA = float(input("what was your gpa? "))
low = float(input("what was your lowest grade? "))

if GPA > 3.00 and low > .5:
    honour_roll = True
else:
    honour_roll = False

if honour_roll:
    print("you've made honour roll")
else:
    print("im sorry youre so dumb")