sale_prices = [
    5,
    234,
    34,
    56,
    436,
    2,
    80
]

#sorted_list = sale_prices.sort() #sort does not return a value on its own
sorted_list = sorted(sale_prices) #have to put var in argument

print(sorted_list)
print(sale_prices)

#great for not changing order of list but creating a sorted version

sorted_list = sorted(sale_prices, reverse=True) #reverse

print(sorted_list)

#depending on whether you want to mutate list, use sorted or sort