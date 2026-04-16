# APPLICATION OF RECURSION

# DEFINE THE FACTORIAL FUNCTION

def factorial(n):
     # HANDLE VALUE INPUT
     if n < 0:
          print("Error!, No factorial for a negative integer!")

     elif n == 0:       # BASE CASE OF THE FUNCTION
          return 1
     else:
          return n * factorial(n - 1)  # RECURSUVE CASE OF THE FUNCTION
     
# ACCEPT THE USER INPUT
number = int(input("Enter the value of n: "))
result = factorial(number)
print(result)
     