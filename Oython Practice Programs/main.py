
# Reverse a string
text_input = "asdfghjkl"
reversed_text = text_input[::-1]
print("Reversed string:", reversed_text)
print("-" * 40)

# Count Vowels and Consonants
text_vowels = "qwertyuiop"
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in text_vowels if char.isalpha() and char in vowels)
consonant_count = sum(1 for char in text_vowels if char.isalpha() and char not in vowels)
print(f"For string '{text_vowels}': Vowels = {vowel_count}, Consonants = {consonant_count}")
print("-" * 40)

# Check Whether a String Is a Palindrome
palindrome_test = "radar"
cleaned_text = palindrome_test.replace(" ", "").lower()
is_palindrome = cleaned_text == cleaned_text[::-1]
print(f"Is '{palindrome_test}' a palindrome? {is_palindrome}")
print("-" * 40)

# Count Words, Characters, and Spaces
sentence = "ranveersingh is sexy"
words = sentence.split()
total_words = len(words)
total_chars = len(sentence)
total_spaces = sentence.count(" ")
print(f"Sentence: '{sentence}'")
print(f"Words: {total_words} | Characters: {total_chars} | Spaces: {total_spaces}")
print("-" * 40)

# Frequency of Each Character
freq_text = "hello world"
char_count = {}
for char in freq_text:
    char_count[char] = char_count.get(char, 0) + 1
print(f"Character frequencies in '{freq_text}':", char_count)
print("-" * 40)

# Count Word Frequency
word_freq_sentence = "The quick brown fox jumps over the lazy dog the"
words_list = word_freq_sentence.lower().split()
word_count = {}
for w in words_list:
    word_count[w] = word_count.get(w, 0) + 1
print("Word Frequencies:", word_count)
print("=" * 40)


# Basic List Operations
numbers_list = [32, 1122, 3223, 33, 32]
total_sum = sum(numbers_list)
average = total_sum / len(numbers_list)
maximum = max(numbers_list)
minimum = min(numbers_list)
print(f"List: {numbers_list}")
print(f"Sum: {total_sum} | Average: {average} | Max: {maximum} | Min: {minimum}")
print("-" * 40)

# Remove Duplicates preserving order & via Set
dup_list = [1, 2, 2, 3, 4, 4, 5, 1]
unique_ordered = []
for num in dup_list:
    if num not in unique_ordered:
        unique_ordered.append(num)
print("Original:", dup_list)
print("Without duplicates (ordered):", unique_ordered)
print("Without duplicates (set conversion):", list(set(dup_list)))
print("-" * 40)

# Sort a List
unsorted_list = [12, 43, 55, 654, 9, 2]
print("Original list for sorting:", unsorted_list)
print("Ascending:", sorted(unsorted_list))
print("Descending:", sorted(unsorted_list, reverse=True))
print("-" * 40)

# Separate Even and Odd Numbers
mix_numbers = [10, 15, 22, 33, 40, 55, 60]
even_nums = [n for n in mix_numbers if n % 2 == 0]
odd_nums = [n for n in mix_numbers if n % 2 != 0]
print(f"From {mix_numbers}:")
print("Evens:", even_nums)
print("Odds:", odd_nums)
print("-" * 40)

# Demonstrate List Methods
demo_list = [10, 20, 30]
demo_list.append(40)
demo_list.insert(1, 15)
demo_list.remove(20)
popped_val = demo_list.pop()
demo_list.sort()
demo_list.reverse()
print("Final mutated list state:", demo_list)
print("=" * 40)


tpl = (5, 12, 3, 45, 21, 9)
print("Tuple:", tpl)
print(f"Sum: {sum(tpl)} | Max: {max(tpl)} | Min: {min(tpl)} | Length: {len(tpl)}")
print("-" * 40)

# Count Occurrences
tpl_occurrences = (10, 20, 30, 20, 40, 20, 50)
print(f"In {tpl_occurrences}, 20 appears {tpl_occurrences.count(20)} times. First index: {tpl_occurrences.index(20)}")
print("-" * 40)

# Convert List to Tuple and Back
start_list = [1, 2, 3, 4, 5]
converted_tuple = tuple(start_list)
back_to_list = list(converted_tuple)
print(f"List: {start_list} -> Tuple: {converted_tuple} -> List: {back_to_list}")
print("=" * 40)


s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
print("Set 1:", s1)
print("Set 2:", s2)
print("Union:", s1.union(s2))
print("Intersection:", s1.intersection(s2))
print("Difference (s1 - s2):", s1.difference(s2))
print("Symmetric Difference:", s1.symmetric_difference(s2))
print("-" * 40)

# Subset and Superset
set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
print(f"Is {set_a} subset of {set_b}? {set_a.issubset(set_b)}")
print(f"Is {set_b} superset of {set_a}? {set_b.issuperset(set_a)}")
print("=" * 40)


students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90,
    "Eve": 88
}

avg_marks = sum(students.values()) / len(students)
top_student = max(students, key=students.get)
print("Student Marks:", students)
print(f"Average Marks: {avg_marks:.2f}")
print(f"Highest Marks: {top_student} with {students[top_student]} marks.")
print("-" * 40)

# Dictionary Methods
student_profile = {"name": "John", "age": 20, "course": "Python"}
student_profile.update({"grade": "A"})
student_profile.pop("age", None)
print("Updated student profile keys:", list(student_profile.keys()))
print("Updated student profile values:", list(student_profile.values()))