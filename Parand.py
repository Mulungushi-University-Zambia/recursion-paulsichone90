from array import *
# ACCEPT USER INPUT
word = input("Enter a world or phrase: ")
word = word.lower().strip().replace(" ", "")
# CREATE AN ARRAY OF CHARACTERS
char = array('u', word)
reversed_char = char.reverse()
if char == reversed_char :
    print(f"{word} is a Palindrome")
else:
    print(f"{word} is not Palindrome")    
