class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age

    def reduce_wallet(self, drink):
        self.wallet -= drink.price

    def buy_drinks(self, drink, pub):
        self.reduce_wallet(drink)
        pub.increase_till(drink)

    