s = "PYTHON"
# Strings

#1. Slicing s[start:end:step]
print(s[1:4]) #output - YTH
print(s[::2]) #output - PTO 

# Reversing a String
print(s[::-1]) #output - NOHTYP 

# String tools
print(s.upper()) #output - PYTHON
print(s.lower()) #output - python
print(s.capitalize()) #output - Python
print(s.title()) #output - Python
print(s.replace("p", "J")) #output - JYTHON
print(len(s)) #output - 6

# split() breaks a string into a list
#join() joins a list into a string

# Looping through a string

#Visit each character in a string
for cha in "Pune":
  print(cha) #output - P u n e
#With the index too
s = "Hello!"
for i in range(len(s)):
  print(i, s[i]) #output - 0 H 1 e 2 l 3 l 4 o 5 !
  