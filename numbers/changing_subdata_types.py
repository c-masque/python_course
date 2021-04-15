from decimal import Decimal

product_cost = 88.40
commission_rate = 0.08
qty = 450

print(int(product_cost) * qty) #int function does not round up, just cuts off
print(float(qty)) #float function turns to float
print(Decimal(product_cost)) #Decimal when imported converts to Decimal
print(complex(commission_rate)) #scientific rate / complex object