# If Statement
# if condition:
#    statement(s)

age = 20

if age >= 18:
    print("You are eligible to vote")

print("Program finished")

# IF - Else 

marks = 35

if marks >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")

# Nested IF else

age = 16
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID card required")
else:
    print("Entry denied: underage")

# If elif else ladder 

marks = 75

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")

# One Line if else (Ternary)
# value_if_true if condition else value_if_false

age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)



