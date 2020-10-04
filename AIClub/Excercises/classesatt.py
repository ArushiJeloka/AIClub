class Employee: #this is the employee class
    def __init__(self, first, last, pay):     #method
        self.first = first                    #instance
        self.last = last
        self.pay = pay
        self.email = first + '@' + last + '.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last) #the space between the 2 {}'s will print as a whitespace in the output


emp_1 = Employee('Bob', 'Ross', 10000) #instance/object of the employee class
emp_2 = Employee('Tom', 'Brady', 100000) #each attribute matches the conditions on the init

''' The 2 lines of code above do the same thing as the next 8 lines of code
emp_1.first = 'Bob'
emp_1.last = 'Ross'
emp_1.email = 'bob@ross.com' #yes bob did get his own domain
emp_1.pay = 10000

emp_2.first = 'Tom'
emp_2.last = 'Brady'
emp_2.email = 'tom@brady.com' #yes tom did get his own domain
emp_2.pay = 100000
'''
print(emp_1.email)
print(emp_2.email)

# to get the full name, either do code below or check fullname method:
# print('{} {}'.format(emp_1.first, emp_1.last))
print(emp_1.fullname()) #if parenthesis aren't used after fullname, the method will be printed instead of the return value of the method
print(emp_2.fullname())