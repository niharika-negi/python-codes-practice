# ==========================================
# Exercise 1: ATM Withdrawal
# ==========================================

# Question:
# Write a Python program for ATM withdrawal.
#
# Conditions:
# Check whether PIN is correct.
# If PIN is correct:
# Check whether withdrawal amount is a multiple of 100.
# If yes, check whether balance is sufficient.
# If sufficient, withdraw the amount.
# Otherwise print "Insufficient Balance".
# If PIN is incorrect, print "Invalid PIN".


pin = int(input("Enter PIN: "))
balance = 10000

if pin == 1234:
    amount = int(input("Enter withdrawal amount: "))

    if amount % 100 == 0:
        if amount <= balance:
            balance = balance - amount
            print("Withdrawal Successful")
            print("Remaining Balance:", balance)
        else:
            print("Insufficient Balance")
    else:
        print("Amount must be a multiple of 100")
else:
    print("Invalid PIN")


# ==========================================
# Exercise 2: Student Result System
# ==========================================

# Question:
# Write a program that takes marks of 3 subjects.
#
# Conditions:
# If every subject has marks >= 40:
# Calculate percentage.
# If percentage >= 75 -> Distinction
# If percentage >= 60 -> First Division
# If percentage >= 50 -> Second Division
# Otherwise -> Pass
# If any subject is below 40 -> Fail.


maths = int(input("Enter Maths marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))

if maths >= 40 and science >= 40 and english >= 40:

    total = maths + science + english
    percentage = total / 3

    print("Percentage:", percentage)

    if percentage >= 75:
        print("Distinction")
    elif percentage >= 60:
        print("First Division")
    elif percentage >= 50:
        print("Second Division")
    else:
        print("Pass")

else:
    print("Fail")


# ==========================================
# Exercise 3: Bank Loan Eligibility
# ==========================================

# Question:
# A bank gives a loan based on:
# Age must be >= 21.
# If age is valid:
# Salary must be >= ₹25,000.
# If salary is valid:
# Credit score >= 750 -> Loan Approved
# Credit score >= 650 -> Loan Approved with Higher Interest
# Otherwise -> Loan Rejected.


age = int(input("Enter your age: "))
salary = float(input("Enter your salary: "))
credit_score = int(input("Enter credit score: "))

if age >= 21:

    if salary >= 25000:

        if credit_score >= 750:
            print("Loan Approved")

        elif credit_score >= 650:
            print("Loan Approved with Higher Interest")

        else:
            print("Loan Rejected")

    else:
        print("Salary must be at least ₹25,000")

else:
    print("Age must be 21 or above")


# ==========================================
# Exercise 4: E-Commerce Discount
# ==========================================

# Question:
# An online shopping website provides discount based on:
#
# If cart amount >= ₹5000:
# If customer is a premium member:
# Discount = 20%
# Otherwise:
# Discount = 10%
#
# If cart amount < ₹5000:
# If premium member:
# Discount = 5%
# Otherwise:
# No discount.
#
# Print final amount.


cart_amount = float(input("Enter cart amount: "))
premium_member = input("Are you a premium member? (yes/no): ")

if cart_amount >= 5000:

    if premium_member == "yes":
        discount = 20
    else:
        discount = 10

else:

    if premium_member == "yes":
        discount = 5
    else:
        discount = 0

discount_amount = cart_amount * discount / 100
final_amount = cart_amount - discount_amount

print("Discount:", discount, "%")
print("Discount Amount:", discount_amount)
print("Final Amount:", final_amount)


# ==========================================
# Exercise 5: Login + Role Based Access
# ==========================================

# Question:
# Create a login system.
#
# Conditions:
# Check username.
# If username is correct:
# Check password.
# If password is correct:
# Check role:
# "admin" -> Full Access
# "teacher" -> Teacher Dashboard
# "student" -> Student Dashboard
# Anything else -> Invalid Role
# Wrong password -> "Wrong Password"
# Wrong username -> "Invalid Username"


username = input("Enter username: ")

if username == "admin":

    password = input("Enter password: ")

    if password == "admin123":

        role = input("Enter role (admin/teacher/student): ")

        if role == "admin":
            print("Full Access")

        elif role == "teacher":
            print("Teacher Dashboard")

        elif role == "student":
            print("Student Dashboard")

        else:
            print("Invalid Role")

    else:
        print("Wrong Password")

else:
    print("Invalid Username")


# ==========================================
# Exercise 6: Movie Ticket Booking
# ==========================================

# Question:
# Create a ticket booking system.
#
# Conditions:
# Check whether seats are available.
# If available:
# Check customer age.
# If age < 5 -> Free
# If age 5-12 -> 50% discount
# If age > 60 -> 30% discount
# Otherwise -> Full price
# If no seats -> "House Full"


seats = 10
ticket_price = 200

if seats > 0:

    age = int(input("Enter customer age: "))

    if age < 5:
        discount = 100
        print("Ticket is Free")

    elif age <= 12:
        discount = 50

    elif age > 60:
        discount = 30

    else:
        discount = 0

    discount_amount = ticket_price * discount / 100
    final_price = ticket_price - discount_amount

    print("Ticket Price:", ticket_price)
    print("Discount:", discount, "%")
    print("Final Amount:", final_price)

else:
  print("House Full")
    print("House Full")
