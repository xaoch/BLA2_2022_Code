#Create the prices dictionary:
prices={}
#Add values
prices["banana"]=4
prices["apple"]= 2
prices["orange"]= 1.5
prices["pear"]= 3

#Create the stock dictionary
stock={}
#Add values
stock["banana"]= 6
stock["apple"]= 0
stock["orange"] =32
stock["pear"]= 15


#Show all prices and stock

for food in prices:
    print(food)
    print("price: {}".format(prices[food]))
    print("stock: {}".format(stock[food]))

total=0
for food in prices:
    money= prices[food]*stock[food]
    print(money)
    total = total + money

print("The total money is", total)