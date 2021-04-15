import math

loss = -20.25
product_cost = 89.99

#print(abs(loss))
print(math.floor(product_cost)) #int produces same but math.floor clearly shows 'intention' which is considered important
print(math.ceil(product_cost))

print(abs(math.floor(loss))) #negatives do the opposite when math.floor - floor has different priority

print(round(product_cost))
print(math.sqrt(product_cost))
print(math.pow(5, 2)) # also can be (5 ** 2) for precise number and not float