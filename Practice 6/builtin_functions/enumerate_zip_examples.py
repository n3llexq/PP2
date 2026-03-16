names = ["Ali", "Bakhtiyar", "Lera"]
midterm = [8, 10, 10]
for i, name in enumerate(names):
    print(i, name)
print()
for name, mark in zip(names, midterm):
    print(name, mark)
print()

x = "10"
y = 5
z = 2.5

print(type(x))
print(type(y))
print(type(z))
print()
print(int(x))
print(float(y))
print(str(z))