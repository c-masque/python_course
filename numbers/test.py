product_id = 516811 #interger example
sale_price = 12.99 #float - complex decimal calculations should be a decimal import as float is less accurate
tax_percentage = 1/20
product_id_again = 516811
sale_price_again = 4.99

print(sale_price * tax_percentage)

# You need 250 lemons and 36 limes for your leimonade. What's your total number of fruit?

def leimonade(lemons, limes):
    total = 0

    total+= lemons + limes

    return total

print (leimonade(5, 4))