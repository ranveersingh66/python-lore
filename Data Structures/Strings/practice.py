# # Palindrome Checker
# word = input("Enter a word: ")
# if word == word[::-1]:
#   print("Yes its a palindrome")
# else:
#   print("No its not a palindrome")

# #Vowel Counter
# var = input("Enter a name: ")
# vowels = 0
# for ch in var:
#   if ch in "aeiouAEIOU":
#     vowels += 1
# print("Vowels: ", {vowels})

#Initial Generator
name = input("Enter Your full name: ")
initials = ""
for part in name.split():
  initials += part[0].upper() + "."
print(initials)


