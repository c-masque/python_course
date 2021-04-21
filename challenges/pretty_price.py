import math

def money_stealing_pretty_pricer(price, it_makes_cents):
    #print(price)

    if isinstance(it_makes_cents, int):
        it_makes_cents - it_makes_cents * 0.01

    return int(price) + str(it_makes_cents)

    #if isinstance(it_makes_cents, int) == True:
    #    new_decimal_price = '.' + str(it_makes_cents)
    #    new_decimal_price = format(new_decimal_price, '.2f')
    #    print(new_decimal_price)


    #if isinstance(price, int) == True:
    #    new_price = '$' + str(price) + '.' + str(it_makes_cents)
    #    return new_price
    #elif isinstance(price, float) == True:
    #    new_price = int(price)
    #    new_price = '$' + str(new_price) + '.' + str(it_makes_cents)
    #    return new_price
    #else:
    #    print('That is not a valid price...')


print(money_stealing_pretty_pricer(5.15, 99))