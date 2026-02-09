a = 100
b = 200
c = 300

if b > a and c > a:
    print(True)

if a > b and a > c:
    print(False)

is_sunny = True
print(is_sunny)
print(not is_sunny)

age = 18
has_license = True
has_car = False

drive_car = age >= 18 and has_license and has_car
print(drive_car)

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y) 
print(x == y)