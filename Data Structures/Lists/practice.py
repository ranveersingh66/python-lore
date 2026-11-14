# Who scored 70 and above
marks = [12, 34, 76, 55, 87, 90, 77, 54, 70]
above = 0

for i in marks:
  if i >= 70:
    above += 1

print("those who scored 70 and above: ", above)

#Average and Above-Average Count

avg = sum(marks) / len(marks)
count = 0

for m in marks:
  if m > avg:
    count += 1

print("average: ", avg)
print("Above average: ", count)

