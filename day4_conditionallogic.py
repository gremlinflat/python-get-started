price = input("How much do you pay? ")
price = float(price)

if price >= 10000 :
    tax = .07
else:
    tax = .01
tax = tax * price
price = price + tax

province = input("Where do you live in? " )

if province.lower() == "banten" :
    price = price - 1000
elif province.lower() == "jakarta" :
    price = price - 500
elif province.lower() == "jabar" :
    price = price - 100
else :
    price = price - 1

print(f"How much should you pay = {price}")