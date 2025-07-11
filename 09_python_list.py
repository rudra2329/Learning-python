# 1. Creating and printing a list
fruits = ["apple", "banana", "mango"]
print("Fruits List:", fruits)

# 2. Accessing elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# 3. Modifying list
fruits[1] = "orange"
print("After modification:", fruits)

# 4. Adding elements
fruits.append("grape")             # Add to end
fruits.insert(1, "kiwi")           # Insert at index 1
print("After adding:", fruits)

# 5. Removing elements
fruits.remove("apple")             # Remove by value
fruits.pop()                       # Remove last item
fruits.pop(0)                      # Remove by index
print("After removing:", fruits)

# 6. List functions
numbers = [5, 3, 8, 2]
print("\nNumbers:", numbers)
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Sum:", sum(numbers))
print("Length:", len(numbers))

# 7. Looping through a list
print("\nAll fruits:")
for fruit in fruits:
    print(fruit)

# -------------------------------
# Practice Problems
# -------------------------------

# 1. Favorite movies
movies = ["Inception", "3 Idiots", "KGF", "Interstellar", "Bahubali"]
print("\nMy favorite movies:", movies)

# 2. Add a new movie
movies.append("Jawan")
print("After adding a movie:", movies)

# 3. Remove a movie
movies.remove("KGF")
print("After removing a movie:", movies)

# 4. List of numbers
numbers = [10, 25, 7, 40, 15]
print("\nNumbers:", numbers)
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))
print("Count:", len(numbers))

# 5. Print each element using a loop
print("\nPrinting all numbers:")
for num in numbers:
    print(num)
