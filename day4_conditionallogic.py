price = input("How much do you pay? ")
price = float(price)

if price >= 1.00 :
    tax = .07
else:
    tax = .01
tax = tax * price
price = price + tax
print(f"How much should you pay = {price}")