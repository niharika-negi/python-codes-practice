# Python Loop Exercises


# Exercise 1: Print all even numbers from 1 to 20

for i in range(1, 21):
    if i % 2 == 0:
        print(i)


# Exercise 2: Print all odd numbers from 1 to 20

for i in range(1, 21):
    if i % 2 != 0:
        print(i)


# Exercise 3: Print multiples of 5 from 5 to 50

for i in range(5, 51, 5):
    print(i)


# Exercise 4: Find the sum of numbers from 1 to 10

sum = 0

for i in range(1, 11):
    sum = sum + i

print("Sum =", sum)


# Exercise 5: Find the sum of even numbers from 1 to 100

sum = 0

for i in range(1, 101):
    if i % 2 == 0:
        sum = sum + i

print("Sum of even numbers =", sum)


# Exercise 6: Find the sum of odd numbers from 1 to 100

sum = 0

for i in range(1, 101):
    if i % 2 != 0:
        sum = sum + i

print("Sum of odd numbers =", sum)


# Exercise 7: Print the multiplication table of 7

for i in range(1, 11):
    print(7, "x", i, "=", 7 * i)


# Exercise 8: Take a number from the user and print its multiplication table

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# Exercise 9: Print numbers from 1 to 100 that are divisible by both 3 and 5

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)


# Exercise 10: Count even and odd numbers between 1 and 50

even_count = 0
odd_count = 0

for i in range(1, 51):
    if i % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

print("Even numbers =", even_count)
print("Odd numbers =", odd_count)
