# Recursive factorial function

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

r = factorial(5)
print(r)

