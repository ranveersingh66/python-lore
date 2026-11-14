#The most used box in Python: an ordered, changeable collection of anything

#Lists methods

marks = [12, 32, 22, 54, 32, 99, 15]

marks.append(70) #adds 70 at the end of the list
marks.insert(1, 96) #adds 96 at index 1
marks.remove(32) #removes the first occurrence of 32
marks.pop() # removes the last element of the list
marks.sort() #sorts the list in ascending order
marks.reverse() #reverses the list


# looping over lists

for mark in marks:
  print(mark) # prints each element of the list

sum(marks) # returns the sum of all elements in the list
min(marks) # returns the minimum value in the list
max(marks) # returns the maximum value in the list
