# Day 8 – Python Functions (Part 2)

# 1. Default Arguments
def greet(name="Rudra"):
    print("Hello", name)

greet()            # Output: Hello Rudra
greet("Siva")      # Output: Hello Siva

print("\n")

# 2. Keyword Arguments
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(age=18, name="Rudra")

print("\n")

# 3. Variable-Length Arguments - *args
def add_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print("Sum of all numbers:", add_all(1, 2, 3, 4))  # Output: 10

# *args Practice: Multiply all numbers
def multiply_all(*args):
    result = 1
    for num in args:
        result *= num
    return result

print("Product of all numbers:", multiply_all(2, 3, 4))  # Output: 24

print("\n")

# 4. Variable-Length Keyword Arguments - **kwargs
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Rudra", age=18, course="Python")

# **kwargs Practice: Student Profile
def student_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("\nStudent Profile:")
student_profile(name="Rudra", age=18, course="Python", rank="Top 3")

print("\n")

# 5. Scope of Variables
x = "Rudra"

def change_name():
    x = "Sivarudra"
    print("Inside function:", x)

change_name()
print("Outside function:", x)  # x remains "Rudra" globally

print("\n")

# Practice with Default Argument
def welcome(name="Guest"):
    print("Welcome", name)

welcome()
welcome("Rudra")
