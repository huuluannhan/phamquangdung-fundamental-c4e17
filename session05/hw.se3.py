price={
"banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3
}
stock={"banana": 6,
"apple": 0,
"orange": 32,
"pear": 15
}
for keys in price:
    print(keys)
    print("price: ",price[keys])
    print("stock",stock[keys])
    print("*********")
total=0
for keys in price:
    total=total+price[keys]*stock[keys]
print("My total: ",total)
