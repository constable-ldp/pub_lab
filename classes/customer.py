class Customer:
    def __init__(self, name, wallet, age, drunkenness):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = drunkenness

    def reduce_wallet(self, drink):
        self.wallet -= drink.price

    def buy_drinks(self, drink, pub, customer):
        if pub.check_underage(customer) or self.drunkenness > 10 or self.wallet < drink.price:
            return
        self.reduce_wallet(drink)
        pub.increase_till(drink)
        self.drunkenness += drink.alcohol_level

    