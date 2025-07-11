# 1. List Methods
fruits = ["apple", "banana", "cherry", "banana"]
print("Original:", fruits)

fruits.append("orange")
fruits.insert(1, "kiwi")
fruits.remove("banana")
fruits.pop()
fruits.sort()
print("Sorted:", fruits)

fruits.reverse()
print("Reversed:", fruits)

# 2. List Comprehension
squares = [i*i for i in range(1, 11)]
print("\nSquares 1–10:", squares)

even_numbers = [i for i in range(1, 21) if i % 2 == 0]
print("Even numbers 1–20:", even_numbers)

# Names that start with A
names = ["Anu", "Ravi", "Arun", "Kavi", "Abhi", "Latha"]
a_names = [name for name in names if name.startswith("A")]
print("Names starting with A:", a_names)

# Practice Task
print("\n--- Practice Task ---")
name_list = ["Kiran", "Divya", "Nila", "Bala", "Arun"]
print("Original Names:", name_list)

name_list.append("Meena")
name_list.insert(2, "Raju")
name_list.remove("Nila")
name_list.pop()
name_list.sort()

print("After all operations:", name_list)
