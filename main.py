name = input("Enter the name: ")
age = int(input("Enter the age: "))
college = input("Enter the college name: ")

mark1 = int(input("Enter mark 1: "))
mark2 = int(input("Enter mark 2: "))
mark3 = int(input("Enter mark 3: "))

total = mark1 + mark2 + mark3
average = total / 3

print("\n--- Student Details ---")
print("Name:", name)
print("Age:", age)
print("College:", college)

print("Mark 1:", mark1)
print("Mark 2:", mark2)
print("Mark 3:", mark3)

print("Total Marks:", total)
print("Average Marks:", average)
