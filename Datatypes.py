Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #datatypes
>>> a=4
>>> type(a)
<class 'int'>
>>> b=100
>>> type(b)
<class 'int'>
>>> c=8.9
>>> type(c)
<class 'float'>
>>> d="code"
>>> type(d)
<class 'str'>
>>> f='''python'''
>>> type(f)
<class 'str'>
>>> x=5+9j
>>> type(x)
<class 'complex'>
>>> y=3j+6
>>> type(y)
<class 'complex'>
>>> z=6j
>>> type(z)
<class 'complex'>
>>> a=6+3i
SyntaxError: invalid decimal literal
>>> b=j
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    b=j
NameError: name 'j' is not defined
>>> b="j"
>>> type(b)
<class 'str'>
>>> a=True
>>> type(a)
<class 'bool'>
>>> b=False
>>> type(b)
<class 'bool'>
>>> b=false
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    b=false
NameError: name 'false' is not defined. Did you mean: 'False'?
>>> a="True"
>>> type(a)
<class 'str'>
