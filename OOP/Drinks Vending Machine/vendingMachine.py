class VendingMachine:
    def __init__(self, size):
        self.content = []                  # list to store drinks objects in the vending machine 
        self.size = size                   # Maximum number of drinks the vending machine can hold


    def add_drink(self, drink):
        if len(self.content) < self.size:
            self.content.append(drink)       # Add a drink to the vending machine if there is space
        else:
            print("Vending machine is full. Cannot add more drinks.")

    def remove_drink(self, index):
        if 0 <= index < len(self.content):
            return self.content.pop(index)   # Remove and return a drink from the vending machine by index
        else:
            print("Invalid index. Cannot remove drink.")
            return None

    def verify_drink_quality(self):
        """
        This method checks that none of the drinks are out of date. It returns a list of all the drinks that are out of date.
        """
        out_of_date_drinks = [drink for drink in self.content if expiration_date == getattr(drink, 'expiration_date', None) and expiration_date < datetime.now()]
        # for drink in self.content:
        #     if drink.is_out_of_date():
        #         out_of_date_drinks.append(drink)
        return out_of_date_drinks

    def next_day(self):
        """
        This method simulates the passage of one day. It should update the expiration date of all drinks in the vending machine.
        """
        for drink in self.content:
            drink.next_day()
            self.verify_drink_quality()  # remove out of date drinks after updating expiration dates.and return the list of out of date drinks


# Instantiating drinks 

first_drink = Drink(350, 14)             # a drink of 350ml that expires in 14 days
first_juice = Juice(1000)                                 # a juice of 1000ml
first_dataCola_can = DataCola('can')                      # a DataCola in a can
first_dataCola_bottle = DataCola('bottle')                # a DataCola in a bottle

# Instantiating a vending machine with a size of 10

vending_machine = VendingMachine(30)

# Adding drinks to the vending machine

vending_machine.add(first_drink)
vending_machine.add(first_juice)
vending_machine.add(first_dataCola_can)
vending_machine.add(first_dataCola_bottle)



