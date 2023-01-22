def priceCheck(products, productPrices, productSold, soldPrice):
    if not len(products) > 0 or not len(products) < 100 or len(products) != len(productPrices) or not \
            len(productSold) > 0 or not len(productSold) < 100 or len(productSold) != len(soldPrice):
        return "incorrect arguments"
    incorrect_prices = 0
    for index, product_sold in enumerate(productSold):
        try:
            actual_price = productPrices[products.index(product_sold)]
            if actual_price < 1 or actual_price > 100000:
                return "incorrect prices values"
        except:
            return "incorrect productSold names"
        sold_price = soldPrice[index]
        if sold_price < 1 or sold_price > 100000:
            return "incorrect prices values"
        if actual_price != sold_price:
            incorrect_prices += 1
    return incorrect_prices


print(priceCheck(
    ['rice', 'sugar', 'wheat', 'cheese'],
    [16.89, 56.92, 20.89, 345.99],
    ['rice', 'cheese'],
    [18.99, 400.89]
))
