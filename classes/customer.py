class Customer:
    def __init__(self, name, wallet, age, drunkenness):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = drunkenness

    def reduce_wallet(self, drink):
        self.wallet -= drink.price
    
    def increase_drunkenness(self, drink):
        self.drunkenness += drink.alcohol_level

    def buy_drinks(self, drink, pub, customer):
        if pub.check_underage(customer) or self.drunkenness > 10 or self.wallet < drink.price:
            return
        self.reduce_wallet(drink)
        pub.increase_till(drink)
        self.increase_drunkenness(drink)
        pub.decrease_stock(drink)

    def buy_food(self, food, pub):
        if self.wallet < food.price:
            return
        self.reduce_wallet(food)
        pub.increase_till(food)
        self.drunkenness -= food.rejuvenation_level
        if self.drunkenness <= 0:
            self.drunkenness = 0