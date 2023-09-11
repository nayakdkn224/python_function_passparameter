price = input("enter the price ($):")
tax = input("enter the tax rate(%):")
net_price = int(price) * int(tax) / 100
print(f'the net price is ${net_price}')
print(net_price)
print(type(price))
print(type(tax))
print(type(net_price))
