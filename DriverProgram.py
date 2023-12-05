# driver_program.py
from ClassDefinitionModule import fooditems

def create_object_list():
    # Function to create a list of objects
    object_list = []
    num_items = 0

    # Prompt user for the number of items
    while num_items < 1:
        try:
            num_items = int(input("How many items will you order today (at least 1): "))
            if num_items < 1:
                print("Number of items must be at least 1.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Loop to gather all necessary inputs
    for _ in range(num_items):
        food_name = input("Enter the name of the item: ")
        pounds = 0

        # Input validation for pounds
        while pounds <= 0:
            try:
                pounds = float(input("Enter the amount of the item in pounds (greater than 0): "))
                if pounds <= 0:
                    print("Please enter a valid amount (greater than 0).")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        # object creation and append to the list
        food_item = fooditems(food_name, pounds)
        object_list.append(food_item)

    return object_list

def display_object_list(object_list):
    print(f"Here's a summary of the items purchased")
    print(f"-------------------------------------")
    # Function to display the contents of the list
    for food_item in object_list:
        print(f"Item: {food_item._food}, Amount ordered: {food_item._pounds} pounds, "
              f"Price per Pound: ${food_item._standard_price:.2f}, "
              f"Price of order: ${food_item.cost():.2f}")

def calculate_total_cost(object_list):
    # Function to calculate the total cost of all items
    total_cost = sum(food_item.cost() for food_item in object_list)
    return total_cost

def main():
    # Main function
    items_list = create_object_list()
    display_object_list(items_list)
    total_cost = calculate_total_cost(items_list)
    print(f"\nTotal Cost of All Items: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
