'''
recursion is when a function is called from itself infinitely
ex: def hi()
         print("Hello!")
         hi()
    hi()

In the recursion code above, you're calling the function hi from within the function hi, printing "Hello!" 'infinitely' many times in theory

The default limit of recursion is 1000. This can be change by customization

Want to change recursion limit? Try:
   import sys
   sys.setrecursionlimit(*enter limit number here*)

Want to test the limit of recursion? Try:
   print(sys.getrecursionlimit())

Now, using recursion, try getting the factorial of a number which is input by the user and check it with code below
'''

n = int(input("Enter integer: "))
def factorial(n):
    if(n == 0):
        return 1
    return n * factorial(n-1)
answer = factorial(n)
print(answer)