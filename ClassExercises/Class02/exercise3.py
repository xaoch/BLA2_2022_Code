shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


def compute_bill(food):
    total=0
    for x in food:
        price= prices[x]
        if stock[x]>0:
           total=total +price
           stock[x]=stock[x] -1
    print(total)

compute_bill(shopping_list)