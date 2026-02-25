Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#conditions
#if-condition by using comparison operators
#<,>,<=,>=,!=,==
a=2
b=4
if a<b:
    print("True")

    
True
a=2
b=4
if a>b:
    print("False")

    

a=2
b=4
del a,b
a=4
b=2
if a>b:
    print("True")

    
True
a=4
b=4
if a<=b:
    print("true")

    
true
del a,b
a=8
b=3
if a>=b:
    print("True")

    
True
if a!=b:
    print("Not equal")

    
Not equal
del a,b
a=4
b=4
if a==b:
    print("Equal")

    
Equal
#now with input method
a=int(input("First Number:"))
First Number:10
b=int(input("Second Number:"))
Second Number:20
if a<b:
    print("Ascending Order")

    
Ascending Order
#now for strings.
#for strings, we can only use !=,==.
a="Codegnan"
if a=="codegnan":
    print("Matched")

    
#with input method
    
a=input("Name:")
Name:Hitesh
if a=="Hitesh":
    print("Valid User")

    
Valid User
#if-condition by using logical operators
#and, or, not.
a=5
b=9
if a<b and b>a:
    print("True")

    
True
a=7
b=11
if a<=b and b>=a:
    print("True")

    
True
a=5
b=7
if a==b or a!=b:
    print("Passes")

    
Passes
a=3
b=8
if not a>b:
    print("opposite of True")

    
opposite of True
a=5
b=4
if not a==b or a!=b:
    print("opposite of not equal")

    
opposite of not equal
#with input function.
a=input("Vignan")
Vignan
b=input("Vignan")
Vignan
if not a!=b:
    print("That's True")

    
That's True
#if-condition using identify operators
#is, is not.
a=7
if type(a) is int:
    print("It is Int")

    
It is Int
if type(a) is not int:
    print("It is not Int")

    
del a
a="codegnan"
if len(a) is 8:
    print("Yes")

    
Yes
if type(a) is str:
    print("True")

    
True
a=6
b=5
if bool(a>b) is True:
    print("True")

    
True
a=5
b=5
if bool(a!=b or a==b) is True:
    print("true")

    
true
if bool(a!=b) is True:
    print("True")

    
a=6+5j
if type(a) is complex:
    print("True")

    
True
a=6.5
b=6.235
if a>b is True:
    print(a)

    
if type(a,b) is float:
    print("true")

    
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    if type(a,b) is float:
TypeError: type() takes 1 or 3 arguments
c =7.8
if type(a,b,c) is float:
    print("True")

    
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    if type(a,b,c) is float:
TypeError: type.__new__() argument 1 must be str, not float
del a,b
if type(c) is float:
    print("True")

    
True
#using input function.
a=int(input("First Number"))
First Number 10
b=int(input("Second Number:"))
Second Number:20
if bool(a<b) is not False:
    print("True")

    
True
#if-condition using membership operators
#in, not in.
del a,b
a="hi"
b="bihari"
if a in b:
    return True
SyntaxError: 'return' outside function
>>> 
>>> if a in b:
...     print("True")
... 
...     
>>> del a,b
>>> a="hi"
>>> b="high"
>>> if a in b:
...     print("True")
... 
...     
True
>>> a=[2,5,6,10]
>>> if 25 not in a:
...     print("True")
... 
...     
True
>>> #using input function.
>>> def membership(str):
...     if 20 in str:
...         print("True")
... 
...         
>>> a=str(input("Enter here:"))
Enter here:2,3,4,5,6,7,8,10
>>> if 20 in a:
...     print("False")
... 
...     
Traceback (most recent call last):
  File "<pyshell#177>", line 1, in <module>
    if 20 in a:
TypeError: 'in <string>' requires string as left operand, not int
>>> if 20 in a[]:
...     
SyntaxError: invalid syntax
>>> print(a)
2,3,4,5,6,7,8,10
>>> #using input function.
>>> a=[10,20,30,40,50]
>>> b=int(input("The value:"))
The value:20
>>> if b in a:
...     print("True")
... 
...     
True
