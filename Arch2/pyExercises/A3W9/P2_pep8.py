class Product:
    def __init__(abc, name: str, amount: int, price: float) -> None:
        abc.name = name
        abc.amount = amount
        abc.price = price

    def get_price(abc, buyAmount):
        if buyAmount > 9 and buyAmount < 100:
            costs = buyAmount * abc.price * 0.90  # 10% discount
        elif buyAmount > 99:
            costs = buyAmount * abc.price * 0.80
        else:
            costs = buyAmount * abc.price

        return costs

    def make_purchase(abc, buyAmount):
        abc.amount = abc.amount - buyAmount
        return abc.amount
