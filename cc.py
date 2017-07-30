
exR = float(input("enter exhange rate "))

gdp = float(input("enter amount of holiday money "))
EU = gdp * exR

print (EU)

if EU < 500 :
    print ("you cannot go on holiday yet but soon, soon!")
else:
    print ("Holiday!")
