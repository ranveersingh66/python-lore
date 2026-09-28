# The For loop
#The for loop is used to iterate over a sequence (a list, a string, a range of numbers, etc.).
# for variable in sequence:
#    statement(s)

# For Loop with range()
for i in range(5):
    print(i)

for i in range(2, 10, 2):
    print(i)

#Example (Shopping Bill)
items = ["Rice", "Milk", "Bread"]
prices = [50, 40, 30]

for i in range(len(items)):
    print(items[i], "-> Rs.", prices[i])

# Output- 
#Rice -> Rs. 50
#Milk -> Rs. 40
#Bread -> Rs. 30

# The While Loop
#The while loop repeats a block of code as long as a condition remains True.

count = 1

while count <= 5:
    print("Count is:", count)
    count = count + 1
#output- 
#Count is: 1
#Count is: 2
#Count is: 3
#Count is: 4
#Count is: 5

#Nested Loops
#A loop placed inside another loop is called a nested loop.
#For every single iteration of the outer loop, the inner loop runs completely.

for i in range(3):
    for j in range(2):
        print(i, j)
