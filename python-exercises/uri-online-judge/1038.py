
# order = input().split(" ")

# X, Y = order

# X = int(X)
# Y = int(Y)

X = 4
Y = 3

if X == 1:
    price = 4.00
    total = price * Y
elif X == 2:
    price = 4.50
    total = price * Y
elif X == 3:
    price = 5.00
    total = price * Y
elif X == 4:
    price = 2.00
    total = price * Y
elif X == 5:
    price = 1.50
    total = price * Y


print("Total: R$ {:.2f}".format(total))