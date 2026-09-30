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

# Example (Pattern Printing)
rows = 4
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()

r = 5 
for i in range(1, r+1):
    for j in range(i):
        print("*", end="")
    print()
# Loop Controls-

# Break (stop the loop completely, right now)
for num in range(1, 10):
    if num == 5:
        break
    print(num)
# Output- 1, 2, 3, 4

# Continue (skip the rest of this round, go to the next one)
for num in range(1, 6):
    if num == 3:
        continue
    print(num)
# Output- 1, 2, 4, 5

# Pass (do nothing at all (a placeholder))
for letter in "Python":
    if letter == "h":
        pass   # to be done later
    print(letter)
# Output- 
#p
#y
#t
#h
#o
#n

#example

list = [1, 2, 3, 4, 12, 65, 23, 98, 76]
for i in range(list(0, 8)):
    if i == 12:
        break



