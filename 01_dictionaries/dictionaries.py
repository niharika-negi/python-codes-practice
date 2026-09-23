# 1. Check Student Result

# Question:
# Given a dictionary containing student marks, use a loop to print
# whether each student has Passed or Failed.

# Condition:
# Marks >= 40 -> Pass
# Marks < 40 -> Fail

students = {
    "Rahul": 75,
    "Amit": 32,
    "Priya": 88,
    "Neha": 39,
    "Rohit": 55
}

for name, marks in students.items():
    if marks >= 40:
        print(name, "-> Pass")
    else:
        print(name, "-> Fail")

  # 2. Student Performance Using Nested If

# Question:
# Print the performance category of each student.

# Conditions:
# Marks >= 80 -> Excellent
# Marks >= 60 -> Good
# Marks >= 40 -> Average
# Marks < 40 -> Fail

students = {
    "Rahul": 85,
    "Amit": 35,
    "Priya": 72,
    "Neha": 48
}

for name, marks in students.items():
    if marks >= 80:
        print(name, "-> Excellent")
    elif marks >= 60:
        print(name, "-> Good")
    elif marks >= 40:
        print(name, "-> Average")
    else:
        print(name, "-> Fail")

  # 3. Product Stock Management

# Question:
# A dictionary contains products and their available stock.
# Use a loop and nested conditions to display the stock status.

# Conditions:
# Stock = 0 -> Out of Stock
# Stock <= 5 -> Low Stock
# Stock > 5 -> Available

products = {
    "Laptop": 10,
    "Mouse": 3,
    "Keyboard": 0,
    "Monitor": 7,
    "Printer": 2
}

for product, stock in products.items():
    if stock == 0:
        print(product, "-> Out of Stock")
    elif stock <= 5:
        print(product, "-> Low Stock")
    else:
        print(product, "-> Available")

  # 4. Employee Salary and Department

# Question:
# The following dictionary contains employee salary and department.
# Display the employee category.

# Conditions:
# Salary >= 50,000:
# IT -> Senior IT Employee
# HR -> Senior HR Employee
# Other department -> Senior Employee
#
# Salary < 50,000 -> Junior Employee

employees = {
    "Rahul": {"salary": 60000, "department": "IT"},
    "Amit": {"salary": 40000, "department": "HR"},
    "Priya": {"salary": 70000, "department": "IT"},
    "Neha": {"salary": 45000, "department": "Finance"}
}

for name, details in employees.items():
    salary = details["salary"]
    department = details["department"]

    if salary >= 50000:
        if department == "IT":
            print(name, "-> Senior IT Employee")
        elif department == "HR":
            print(name, "-> Senior HR Employee")
        else:
            print(name, "-> Senior Employee")
    else:
        print(name, "-> Junior Employee")

  # 5. Check Even/Odd Values

# Question:
# Given a dictionary, check whether each value is even or odd.

# Conditions:
# Even and greater than 20 -> Large Even
# Even and <= 20 -> Even
# Odd -> Odd

data = {
    "a": 10,
    "b": 15,
    "c": 25,
    "d": 30,
    "e": 40
}

for key, value in data.items():
    if value % 2 == 0:
        if value > 20:
            print(key, "-> Large Even")
        else:
            print(key, "-> Even")
    else:
        print(key, "-> Odd")
    # 6. Shopping Cart Classification

# Question:
# A dictionary contains products and their prices.

# Conditions:
# Price >= 5000 -> Premium Product
# Price >= 1000 -> Expensive Product
# Price < 1000 -> Affordable Product

products = {
    "Mobile": 15000,
    "Mouse": 500,
    "Laptop": 60000,
    "Keyboard": 1200
}

for product, price in products.items():
    if price >= 5000:
        print(product, "-> Premium Product")
    elif price >= 1000:
        print(product, "-> Expensive Product")
    else:
        print(product, "-> Affordable Product")
    # 7. Student Eligibility

# Question:
# The dictionary contains student attendance and marks.

# Conditions:
# Attendance >= 75:
# Marks >= 40 -> Eligible
# Marks < 40 -> Failed in Exam
# Attendance < 75 -> Not Eligible

students = {
    "Rahul": {"attendance": 85, "marks": 70},
    "Amit": {"attendance": 60, "marks": 80},
    "Priya": {"attendance": 90, "marks": 35},
    "Neha": {"attendance": 78, "marks": 55}
}

for name, details in students.items():
    attendance = details["attendance"]
    marks = details["marks"]

    if attendance >= 75:
        if marks >= 40:
            print(name, "-> Eligible")
        else:
            print(name, "-> Failed in Exam")
    else:
        print(name, "-> Not Eligible")
    # 8. Bank Account Classification

# Question:
# A dictionary contains customer names and account balances.

# Conditions:
# Balance > 0:
# Balance >= 10000 -> Premium Account
# Otherwise -> Regular Account
# Balance = 0 -> No Balance
# Balance < 0 -> Overdraft

accounts = {
    "Rahul": 25000,
    "Amit": 5000,
    "Priya": 0,
    "Neha": -2000
}

for name, balance in accounts.items():
    if balance > 0:
        if balance >= 10000:
            print(name, "-> Premium Account")
        else:
            print(name, "-> Regular Account")
    elif balance == 0:
        print(name, "-> No Balance")
    else:
        print(name, "-> Overdraft")
    
    
      
