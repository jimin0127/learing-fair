import datetime


def calculator_price(price, quality, buy_count, bought_product):
    price = int(price)
    original_price = int(bought_product["price"])

    discount_rate_by_quality = get_discount_rate_by_quality(quality)
    discount_rate_by_category = get_discount_rate_by_category(bought_product["category"])
    discount_rate_by_bought_year = get_discount_rate_by_bought_year(int(bought_product["bought_year"]))

    total_discount_rate = discount_rate_by_quality + discount_rate_by_category + discount_rate_by_bought_year

    discount_amount = original_price * total_discount_rate / 100
    discounted_price_per_item = price - discount_amount

    if discounted_price_per_item < price * 0.60:
        discounted_price_per_item = price * 0.60

    return int(discounted_price_per_item * buy_count)

def get_discount_rate(quality, bought_product):
    discount_rate_by_quality = get_discount_rate_by_quality(quality)
    discount_rate_by_category = get_discount_rate_by_category(bought_product["category"])
    discount_rate_by_bought_year = get_discount_rate_by_bought_year(int(bought_product["bought_year"]))

    total_discount = discount_rate_by_quality + discount_rate_by_category + discount_rate_by_bought_year
    print("adfadf", total_discount)

    return total_discount

def get_discount_rate_by_quality(quality):
    if quality == "상":
        return 3
    elif quality == "중":
        return 2
    elif quality == "하":
        return 1
    else:
        return 0

def get_discount_rate_by_category(category):
    if category == "아우터":
        return 20
    elif category == "상의":
        return 15
    elif category == "바지":
        return 15
    elif category == "원피스/스커트":
        return 10
    elif category == "신발":
        return 10
    elif category == "악세사리":
        return 5
    else:
        return 0

def get_discount_rate_by_bought_year(bought_year):
    now_year = datetime.datetime.now().year
    return 10 - (now_year - int(bought_year))