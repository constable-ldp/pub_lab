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

    def find_drink_by_name(self, drink_name):
        for drink in self.drinks:
            if drink.name == drink_name:
                return drink
        return None

    def decrease_stock(self, drink_name):
        try:
            self.find_drink_by_name(drink_name).stock -= 1
        except:
            return 

    def total_stock_value(self):
        total = 0
        for drink in self.drinks:
            total += drink.price * drink.stock
        return total