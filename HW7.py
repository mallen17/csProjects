# File: HW7.py
# Author: Max Allen
# UT EID: mca2773
# Course: CS303E
# I will utilize classes to go shopping

class ItemToPurchase:
    """
    Creates an item with name, price, and quantity.

    Attributes
    ----------
    name: str
        Name of the item you create
    price: float
        Price of the item
    """
    
    def __init__(self, name, price, quantity):
        """
        Initializes the ItemToPurchase class by assigning variables

        Parameters
        ----------
        name: str
            Name of the item you create
        price: float
            Price of the item
        quantity: int
            Amount of the item
        """

        self.name = name
        self.price = price
        self.__quantity = quantity

    def get_quantity(self):
        """
        Gives the user the private quantity value

        Returns
        -------
        self.__quantity: int
            Existing quantity value
        """

        return self.__quantity
    
    def set_quantity(self, new_quantity):
        """
        Changes the existing quantity value to whatever parameter is given

        Parameters
        ----------
        new_quantity: int
            Quantity that the user wants to change to in an item
        """

        self.__quantity = new_quantity

    def __str__(self):
        """
        Creates a string for the class that prints all important values

        Returns
        -------
        String: str
            A sentence containing all values plus a calculated total price.
        """

        total_price = self.__quantity * self.price
        return(f"{self.name}: {self.__quantity} @ ${self.price:.2f} = ${total_price:.2f}")
    
class ShoppingCart:
    """
    Creates an empty cart which you can add items from the ItemToPurchase class into

    Attributes
    ----------
    customer_ID: int
        An identifier for the unique cart
    cart_items: list
        A list containing ItemToPurchase values to represent a shopping cart
    """

    def __init__(self, customer_ID):
        """
        Initializes a shopping cart by creating ID and cart values

        Parameters
        ----------
        customer_ID: int
            An identifier for the unique cart
        """

        self.customer_ID = customer_ID
        self.cart_items = []
    
    def add_item(self, item):
        """
        Adds an item to the cart

        Parameters
        ----------
        item: class ItemToPurchase object
            item to be appended to the cart_items list
        """

        self.cart_items.append(item)

    def remove_item(self, item):
        """
        Removes an item from the shopping cart

        Parameters
        ----------
        item: class ItemToPurchase object
            item to be removed from the cart_items list
        """

        self.cart_items.remove(item)

    def change_quantity(self, name, quant):
        """
        Changes the quantity of an item in the cart

        Parameters
        ----------
        new_name: str
            Name of the item you want to modify
        quant: int
            New quantity value
        """

        for item in self.cart_items:
            if item.name == name:
                item.name = name
                item.set_quantity(quant)

    def print_cart(self):
        """
        Prints a string containing relevant value of the cart
        """
        total_price = 0
        print(f"Shopping Cart for Customer: {self.customer_ID}")
        for item in self.cart_items:
            print(item)
            total_price += item.get_quantity() * item.price
        print(f"TOTAL: ${total_price:.2f}")
    
def main():
    item1 = ItemToPurchase("Potato Chips", 3.49, 1)
    item1.set_quantity(2)
    item2 = ItemToPurchase("Soda", 1.50, 1)
    #print(item1)
    #print(item2)
    cart = ShoppingCart(987654)
    cart.add_item(item1)
    cart.add_item(item2)
    cart.print_cart()
    cart.remove_item(item1)
    print()
    cart.print_cart()
    cart.change_quantity("Soda", 3)
    print()
    cart.print_cart()

if __name__ == "__main__":
    main()