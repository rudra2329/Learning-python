#Code_01
fruits = ["apple", "banana", "mango"]
print(fruits)
print(fruits[0])   # First item
print(fruits[1])   # Second itemfruits[1] = "orange"
print(fruits)
fruits.append("grape")
print(fruits)

#code_02
movies = ["Leo", "Master", "Vikram", "Kaithi", "Beast"]

print("Original list:", movies)

movies[1] = "Bigil"  # Change 2nd movie
movies.append("Jailer")  # Add a movie
movies.remove("Beast")  # Remove a movie

print("Updated list:", movies)
