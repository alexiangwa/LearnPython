#print("welcome to python scripting")
#print("we are working with special characters")
print("welcome to python scripting,\nwe are working with special characters")
>>> print("welcome to python scripting,\nwe are working with special characters")
welcome to python scripting,
we are working with special characters
>>> print("hello world")
hello world
>>> print("hello \bworld")
helloworld
>>> print("hello \b\bworld")
hellworld
>>> print("hello \b\b\bworld")
helworld
>>> print("hello \tworld")
hello   world
>>> print('python's class')
  File "<stdin>", line 1
    print('python's class')
                  ^
SyntaxError: invalid syntax
>>> print('python\'s class')
python's class
>>> print("this is a "python" class")
  File "<stdin>", line 1
    print("this is a "python" class")
                      ^
SyntaxError: invalid syntax
>>> print("this is a \"python\" class")
this is a "python" class
>>> print("C:\Users\American\Desktop\PythonScripts\New")
  File "<stdin>", line 1
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> print("C:\\Users\\American\\Desktop\\PythonScripts\\New")
C:\Users\American\Desktop\PythonScripts\New
