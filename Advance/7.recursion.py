#Recursion: A function calling itself

def countdown(n):
    if n == 0:
        return

    print(n)
    countdown(n - 1)

countdown(5)
"""
output:
5
4
3
2
1
"""

#factorial method
def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))
#output: 120
