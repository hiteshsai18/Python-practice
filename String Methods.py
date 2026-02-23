Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#len()
a="coegnan"
len(a)
7
a="Python course"
len(a)
13
c=""
len(c)
0
d=" "
len(d)
1
len("Python")
6
len(" ")
1
#count
a="twinkle twinkle little star"
count(a)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
#shouln't o this as count is a built in function.
a.count("twinkle")
2
a.count("i")
3
a.count(" ")
3
a="she sells seashells on the seashore"
a.count("s")
8
a.count("e")
7
#find a string
a="codegnan"
a.find("n")
5
a[5]+a[7]
'nn'
b="code"
b.find("e")
3
b[3]
'e'
#to print multiple ientical characters
c[2:4]
''
c="hello'
SyntaxError: unterminated string literal (detected at line 1)
c="hello"
c[2:4]
'll'
#escape sequences
#\n->new line
#\t->tab space
a=
SyntaxError: invalid syntax
a="name\nmobile\tMail Id\nCity"
print(a)
name
mobile	Mail Id
City
b="Name: Hitesh Sai\nMobile:38287983\tMail Id:hitesh@gmail.com\nCity:Eluru"
print(b)
Name: Hitesh Sai
Mobile:38287983	Mail Id:hitesh@gmail.com
City:Eluru
b="Name: Hitesh Sai\nMobile:38287983\t\t\tMail Id:hitesh@gmail.com\nCity:Eluru"
print(b)
Name: Hitesh Sai
Mobile:38287983			Mail Id:hitesh@gmail.com
City:Eluru
#replace
a="wait till you succeed"
a.replace("wait","work")
'work till you succeed'
a="wait wait till you succeed"
a.replace("wait","work")
'work work till you succeed'
a="wait wait till you succeed"
a.replace("wait","work",1)
'work wait till you succeed'
a.remove("work")
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    a.remove("work")
AttributeError: 'str' object has no attribute 'remove'
#upper()
a="code"
a.upper()
'CODE'
#lower()
b="PYTHON"
b.lower()
'python'
c="apple"
c.capitalize()
'Apple'
#capitalize method prints only the first letter as uppercase.
#if you want to print first letter of every word in a string as capital then,
c.title()
'Apple'
c="python course"
c.title()
'Python Course'
c="i'm in class"
c.title()
"I'M In Class"
#isupper, #islower, #isalpha, #isigit
a="python"
a.isupper()
False
a.islower()
True
a.isalpha()
True
a.isigit
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    a.isigit
AttributeError: 'str' object has no attribute 'isigit'. Did you mean: 'isdigit'?
a.isdigit()
False
a="5678"
a.isigit()
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    a.isigit()
AttributeError: 'str' object has no attribute 'isigit'. Did you mean: 'isdigit'?
a.isdigit()
True
#a=5678 won't give true for isigit as it is int not a string.
a="python course"
a.isalpha()
False
#as there is space, it is not considered as alphabets.
a="Python"
a.isupper()
False
a.islower()
False
#isalnum()
a=
SyntaxError: invalid syntax
a="apple"
a.isalnum()
True
a="apple67"
a.isalnum()
True
a="56678"
a.isalnum()
True
#strip()
a="           Hello          "
a.strip()
'Hello'
a="           Hello          "
a.lstrip()
'Hello          '
a="           Hello          "
a.rstrip()
'           Hello'
#split()
a="python java c c++"
a.split()
['python', 'java', 'c', 'c++']
a="i love python"
a.split()
['i', 'love', 'python']
a[3]
'o'
#join()
a="python " "java " "c "
" ".join(a)
'p y t h o n   j a v a   c  '
a="python" " " "java" " " "c"
" ".join
<built-in method join of str object at 0x00007FF949959CC8>
" ".join()
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    " ".join()
TypeError: str.join() takes exactly one argument (0 given)
" ".join(a)
'p y t h o n   j a v a   c'
a="python" "java" "c"
"".join(a)
'pythonjavac'
#concatenation
a"code"
SyntaxError: invalid syntax
a=
SyntaxError: invalid syntax
#concatenation
a="code"
b="gnan"
print(a+b)
codegnan
a="python"
b="course"
print(a+b)
pythoncourse
print(a+" "+b)
python course
fname="Hitesh"
del fname
>>> fname="hitesh"
>>> lname="emmaneni"
>>> print((fname+" "+lname).title())
Hitesh Emmaneni
>>> #formatting
>>> a=5
>>> b=7
>>> print("The sum is",a+b)
The sum is 12
>>> a="Hitesh"
>>> b="Emmaneni"
>>> print("The name is",a+" "+b)
The name is Hitesh Emmaneni
>>> a="diwali"
>>> b="festival"
>>> print("Today is
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print("Today is",a.capitalize()+" "+b)
...       
Today is Diwali festival
>>> #dotformat
...       
>>> #format method
...       
>>> a="Oggy"
...       
>>> b="Jack"
...       
>>> print("Hello {} and {}".format(a,b))
...       
Hello Oggy and Jack
>>> print("Hello {} and {}".format(a,b).upper())
...       
HELLO OGGY AND JACK
>>> #formatting string
...       
>>> a="john"
...       
>>> b="henry"
...       
>>> print(f"Hello {a}{b}")
...       
Hello johnhenry
>>> print(f"Hello {a} Hello {b}".title())
...       
Hello John Hello Henry
>>> #fstring
...       
