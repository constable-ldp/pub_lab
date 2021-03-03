class Pub:
    def __init__(self, till, drinks):
        self.name = 'The Royal Mile'
        self.till = till
        self.drinks = drinks

    def increase_till(self, drink):
        self.till += drink.price

    def add_new_drink(self, drink):
        self.drinks.append(drink)
