# CREATE AN ARRAY OF CHARACTERS
# ACCEPT USER INPUT
word = input("Enter a world or phrase: ")
word = word.lower().strip().replace(" ", "")
char = list(word)
reversed_char = char[: : -1]
if char == reversed_char :
    print(f"{word} is a Palindrome")
else:
    print(f"{word} is not Palindrome")    