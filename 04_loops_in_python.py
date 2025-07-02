#code_01
#using while loop
i = 1
while i <= 5:
    print(i)
    i += 1

#code_02
#using for loop
for i in range(1, 6):
    print(i)

#Code_03
#to find sum of number
n = int(input("Enter a number: "))
total = 0

for i in range(1, n + 1):
    total += i
print("Sum =", total)

#code_04
#num = int(input("Enter a number: "))
for num in range(1, 11):
    print(num, "x", i, "=", num * i)
