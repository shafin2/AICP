# Task 1: Setting up the system and ordering the main items
def display_items(category, items):
    print(f"\n{category} Options:")
    for code, (description, price) in items.items():
        print(f"{code} - {description} (${price:.2f})")

def choose_item(category, items):
    while True:
        display_items(category, items)
        choice = input(f"Choose a {category} (Enter item code): ").upper()
        if choice in items:
            return choice
        else:
            print("Invalid choice. Please enter a valid item code.")

def calculate_computer_price(main_items, prices):
    return sum(prices[category][main_items[category][0]][1] for category in main_items)

def display_order(chosen_items, computer_price):
    print("\nOrder Summary:")
    for category, (item_code, _) in chosen_items.items():
        print(f"{category}: {item_code} - ${computer_price:.2f}")
    print(f"\nTotal Price: ${computer_price:.2f}")


# Task 2: Ordering additional items
def order_additional_items(categories, items):
    chosen_items = {}
    for category in categories:
        choice = input(f"Do you want to purchase additional items from {category}? (yes/no): ").lower()
        if choice == 'yes':
            chosen_item_code = choose_item(category, items[category])
            chosen_items[category] = (chosen_item_code, items[category][chosen_item_code][1])
    return chosen_items


# Task 3: Offering discounts
def apply_discount(computer_price, additional_items):
    discount_rate = 0.05 if len(additional_items) == 1 else 0.10 if len(additional_items) >= 2 else 0
    discount_amount = computer_price * discount_rate
    discounted_price = computer_price - discount_amount
    return discount_amount, discounted_price

# Data for the items
items = {
    'Case': {'A1': ('Compact', 75.00), 'A2': ('Tower', 150.00)},
    'RAM': {'B1': ('8 GB', 79.99), 'B2': ('16 GB', 149.99), 'B3': ('32 GB', 299.99)},
    'Main Hard Disk Drive': {'C1': ('1 TB HDD', 49.99), 'C2': ('2 TB HDD', 89.99), 'C3': ('4 TB HDD', 129.99)},
    'Solid State Drive': {'D1': ('256 GB SSD', 99.99), 'D2': ('512 GB SSD', 149.99)},
    'Second Hard Disk Drive': {'E1': ('1 TB HDD', 49.99), 'E2': ('2 TB HDD', 89.99)},
    'Optical Drive': {'F1': ('DVD-RW', 19.99), 'F2': ('Blu-ray', 59.99)},
    'Operating System': {'G1': ('Windows 10', 129.99), 'G2': ('Linux', 0.00)},
}

# Task 1
chosen_items_task1 = {
    'Case': (choose_item('Case', items['Case']), items['Case']),
    'RAM': (choose_item('RAM', items['RAM']), items['RAM']),
    'Main Hard Disk Drive': (choose_item('Main Hard Disk Drive', items['Main Hard Disk Drive']), items['Main Hard Disk Drive'])
}

computer_price_task1 = calculate_computer_price(chosen_items_task1, items)

display_order(chosen_items_task1, computer_price_task1)

# Task 2
chosen_items_task2 = chosen_items_task1.copy()
additional_items = order_additional_items(['Solid State Drive', 'Second Hard Disk Drive', 'Optical Drive', 'Operating System'], items)
chosen_items_task2.update(additional_items)

computer_price_task2 = calculate_computer_price(chosen_items_task2, items)

display_order(chosen_items_task2, computer_price_task2)

# Task 3
discount_amount, discounted_price = apply_discount(computer_price_task2, chosen_items_task2)

print(f"\nDiscount Applied: ${discount_amount:.2f}")
print(f"Discounted Price: ${discounted_price:.2f}")