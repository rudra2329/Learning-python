# code_1 Simple function without parameters
def greet():
    print("Hello, Rudra!")

greet()  # Call the function


# code_2 Function with one parameter
def greet_name(name):
    print("Hello,", name)

greet_name("Rudra")


# code_3 Function with two parameters and return value
def add(a, b):
    return a + b

result = add(3, 5)
print("Addition:", result)


# Practice Problems

# code_1 Print "Welcome" 3 times using a function
def welcome():
    print("Welcome")

welcome()
welcome()
welcome()


# code_2 Multiply two numbers
def multiply(a, b):
    return a * b

print("Product:", multiply(4, 6))


# code_3 Check if a number is even
def is_even(n):
    return n % 2 == 0

print("Is 7 even?", is_even(7))
print("Is 10 even?", is_even(10))


# code_4 Area of circle
def area_of_circle(r):
    return 3.14 * r * r

print("Area of circle (r=5):", area_of_circle(5))


# code_5 Return maximum of two numbers
def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b

print("Max of 10 and 20:", max_of_two(10, 20))
