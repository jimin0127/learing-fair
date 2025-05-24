import datetime

class PriceCalculator:
    @staticmethod
    def calculate_price(price, condition, buy_count, bought_product):
        price = int(price)
        original_price = int(bought_product["price"])

        discount_rate_by_quality = PriceCalculator._get_discount_rate_by_condition(condition)
        discount_rate_by_category = PriceCalculator._get_discount_rate_by_category(bought_product["category"])
        discount_rate_by_bought_year = PriceCalculator._get_discount_rate_by_bought_year(int(bought_product["bought_year"]))

        total_discount_rate = discount_rate_by_quality + discount_rate_by_category + discount_rate_by_bought_year

        discount_amount = original_price * total_discount_rate / 100
        discounted_price_per_item = price - discount_amount

        # 최소 가격 제한: 기존 가격의 40%
        min_price = price * 0.60
        if discounted_price_per_item < min_price:
            discounted_price_per_item = min_price

        return int(discounted_price_per_item * buy_count)

    @staticmethod
    def _get_discount_rate_by_condition(condition):
        return {
            "상": 3,
            "중": 2,
            "하": 1
        }.get(condition, 0)

    @staticmethod
    def _get_discount_rate_by_category(category):
        return {
            "아우터": 20,
            "상의": 15,
            "바지": 15,
            "원피스/스커트": 10,
            "신발": 10,
            "악세사리": 5
        }.get(category, 0)

    @staticmethod
    def _get_discount_rate_by_bought_year(bought_year):
        now_year = datetime.datetime.now().year
        return 10 - (now_year - int(bought_year))
