# 1. Sum of natural numbers using for loop

num = int(input("Enter a positive integer: "))
sum = 0 
for x in range (1, num+1):
  sum+= x
print("the sum of first", num, "natural numbers is: ", sum)


#2. Factorial of a number using for loop

n = int(input("enter a number for factorial: "))
fac = 1
if n<0:
  print("Factorial Does not exist")
elif n == 0:
  print("Factorial of 0 is 1")
else:
  for i in range(1, n+1):
    fac = fac*i
print("Factorial of ", n, "is: ", fac)


#3. Armstrong Number

a = int(input("Enter a number to check: "))

numstr = str(a)
digits = len(numstr)

sum = sum(int(digits)) ** digits for digit 
