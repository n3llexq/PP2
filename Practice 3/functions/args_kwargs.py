def sum_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num
    print(f"Sum: {total}")

def display_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")
    print()

sum_numbers(10, 20, 30)
sum_numbers(5, 5, 5, 5, 5)
sum_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

display_info(name="John", age=30, city="New York")
display_info(user="admin", access="root", status="active")
display_info(product="Laptop", price=999.99, in_stock=True, brand="Dell")