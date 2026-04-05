class Drink:
    def __init__(self, volume, expiration_date):
        self.volume = volume                     # Volume in milliliters
        self.expiration_date = expiration_date   # Number of days until the drink expires

    def is_out_of_date(self):
        return self.expiration_date < datetime.now()

    def next_day(self):
        if self.expiration_date > 0:
            self.expiration_date -= 1  # Decrease the expiration date by one day

# Defining the juice class that inherits from the Drink class
class Juice(Drink):
    def __init__(self, volume):
        super().__init__(volume, expiration_date=7)  # Juices expire in 7 days

# Defining the DataCola class that inherits from the Drink class
class DataCola(Drink):
    def __init__(self, container_type):
        if container_type == 'can':
            super().__init__(volume=330, expiration_date=30)  # DataCola in a can expires in 30 days
        elif container_type == 'bottle':
            super().__init__(volume=500, expiration_date=60)  # DataCola in a bottle expires in 60 days
        else:
            raise ValueError("Invalid container type. Must be 'can' or 'bottle'.")
            