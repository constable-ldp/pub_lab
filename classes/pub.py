class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def increase_till(self, drink):
        self.till += drink.price

    def add_new_drink(self, drink):
        self.drinks.append(drink)
    
    def check_underage(self, customer):
        if customer.age < 18:
            return True
        return False
