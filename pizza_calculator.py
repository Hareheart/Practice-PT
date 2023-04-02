# This "Pizza Calculator" takes the orders of a set amount of travelers chosen by the users and calculates the total price of all the orders
# The user inputs the size of the pizza and the amount of slices for each individual traveler
# THE PIZZAS ARE SPLIT INTO 8 SLICES EACH


# Defines prices for pizzas depending on size
prices = {"small": 1, "medium": 2.5, "large": 4, "Small": 1, "Medium": 2.5, "Large": 4,}


class Traveler():
    def __init__(self, name: str, size: str, num_slices: int):
        # Initializes name, size and slices for traveler, and uses info to determine sum
        self.name = name
        self.size = size
        self.num_slices = num_slices
        self.total_sum = self.calc_total_sum()

    def set_price(self):
        # Checks what the user's inputted size corresponds with in prices dictionary and returns the corresponding price
        return prices[self.size]

    def num_pizzas(self, num_slices):
        # Checks if there are any remaining slices from a pizza and subtracts them from the total number of slices
        # When num pizzas is defined, one is added to round up to one pizza that used to have remaining slices
        rem_slices = int(num_slices % 8)
        num_slices -= rem_slices
        num_pizzas = (num_slices / 8) + 1
        return num_pizzas

    def calc_total_sum(self):
        # Defines the price based on the size and multiplies it by the number of pizzas to get the total sum
        # Sum is then returned
        price = self.set_price()
        num_pizzas = self.num_pizzas(self.num_slices)
        total_sum = num_pizzas * price
        return total_sum


def main():
    print("")
    # Introduction that informs the user of pizza prices depending on size
    print("Good evening, fellow travelers! You must be exhausted from such a long journey over the Broken Mountains. But fear not! We here at "
          "the Flouncing Fellows has got you covered. Being the most exclusive pizza place across the Veiled Valleys, we have fantastic prices "
          "for immaculate pizza.")
    print("We serve our pizzas either small, medium, or large; the size determines the price. A small pizza costs $1, a medium $2.5, and a large $4.")

    # Initializes a list in which each individual traveler can be stored
    travelers = []

    while True:
        try:
            # initializes integer variable and sets it to user's input
            num_travelers = int(input("Now, how many travelers are you? "))
            break
        except ValueError:
            print("Fellow traveler, please enter a number of people (integer).")

    # Defines sizes
    sizes = ["small", "medium", "large", "Small", "Medium", "Large"]

    take_traveler_orders(travelers, num_travelers, sizes)

    total = calculate_prices(travelers)
    print("")
    print("Your bill will be a sum of " + str(total) + ".")
    print("Pay up, doofuses. ")
    print("")


def take_traveler_orders(travelers, num_travelers, sizes):
    for traveler in range(num_travelers):
        # For each traveler, asks for name, size, and number of slices, and traveler is then appended to list
        print("")
        name = input("What is your name, traveler? ")

        size_choice = input("Hello, " + name + ". What size would you like? ")
        size = choose_size(size_choice, sizes)

        while True:
            try:
                slices = int(input("How many slices would you like? "))
                break
            except ValueError:
                print("Fellow traveler. Were you ever taught basic arithmetics? Because you have to say an integer! ")
        print("")

        traveler = Traveler(name, size, slices)
        print("The price will be $" + str(traveler.total_sum) + ".")
        travelers.append(traveler)


def choose_size(size_choice, sizes):
    while True:
        if size_choice not in sizes:
            print("Fellow traveler, please enter one of the three sizes available.")
            size_choice = input("What size would you like? ")
        elif size_choice in sizes:
            break
    return size_choice


def calculate_prices(travelers):
    # Defines a total sum, iterates through each traveler's bill and adds it to the total sum, which is then returned
    total_price = 0
    for traveler in travelers:
        traveler_price = traveler.calc_total_sum()
        total_price += traveler_price
    
    return total_price


if __name__ == "__main__":
    main()