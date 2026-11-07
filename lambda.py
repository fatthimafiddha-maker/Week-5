square = lambda x: x * x

print(square(5))

add = lambda a, b: a + b

print(add(10, 20))

check = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check(7))

largest = lambda a, b: a if a > b else b

print(largest(25, 40))

students = [("John", 85), ("Alice", 92), ("Bob", 75)]

result = sorted(students, key=lambda x: x[1])

print(result)