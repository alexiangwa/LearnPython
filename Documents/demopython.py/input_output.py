
'''
 C:\Users\American\Documents\demopython.py> vim input_output.py    
PS C:\Users\American\Documents\demopython.py> python input_output.py
Enter a value: 45
the value of a is: 45 and type is: <class 'str'>
PS C:\Users\American\Documents\demopython.py> cat input_output.py    
#simple arimethic calculator
#simple arimethic calculator
a=input("Enter a value: ")
b=input("Enter b value: ")
#print(f'the addition of {a} and {b} is: {result}')
print(f'the value of a is: {a} and type is: {type(a)}')
PS C:\Users\American\Documents\demopython.py> python input_output.py
Enter a value: 4
Enter b value: 5
the value of a is: 4 and type is: <class 'str'>


>>> x=input("Enter x ")
Enter x 56
>>> type(x)
<class 'str'>
>>> x=int(input("Enter x"))
Enter x56
>>> print(type(x))
<class 'int'>
>>> x
56
>>> x=eval(input("Enter x:"))
Enter x:3
#simple arimethic calculator
a=eval(input("Enter a value: "))
b=eval(input("Enter b value: "))
>>> print(type(x))
<class 'float'>
>>> x=eval(input("Enter x:"))
Enter x: "Hi"
>>> print(type(x))
<class 'str'>
'''


#simple arimethic calculator
a=eval(input("Enter a value: "))
b=eval(input("Enter b value: "))
result=a+b
print(f'the addition of {a} and {b} is: {result}')
print(f'the value of a is: {a} and type is: {type(a)}')
