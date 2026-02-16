def multiply_numbers(x, y):
    return x * y

def combine_strings(str1, str2):
    return f"{str1} {str2}"

def is_greater_than_limit(value, limit=0.8):
    return value > limit

product = multiply_numbers(10, 2.5)
print(product)

combined = combine_strings("Hello", "World")
print(combined)

is_greater = is_greater_than_limit(0.95)
print(is_greater)