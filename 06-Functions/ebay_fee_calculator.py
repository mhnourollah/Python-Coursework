def calc_ebay_fee(sell_price):
    fee = 0.50

    if sell_price <= 50:
        fee += sell_price * 0.13
    elif sell_price <= 1000:
        fee += (50 * 0.13) + ((sell_price - 50) * 0.05)
    else:
        fee += (50 * 0.13) + ((1000 - 50) * 0.05)
        fee += ((sell_price - 1000) * 0.02)

    return fee

price = float(input())

print(calc_ebay_fee(price))
