# APPLICATION OF RECURSION
# DEFINE THE FIBONACCI FUNCTION
def fibonacci(n):
    if n < 0:       #HANDLE VALUE  INPUT
        print("Error!, no fibonaci oof negative numbers ")

    elif n == 0:     # BASE CASE
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)    # RECURSIVE CASE

# ACCEPT THE USER INPUT
number = int(input("Enter the value of n: "))
result = fibonacci(number)
print(result)
