Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a=[3,4.5,"python",6+9j,True,False]
print(a)
[3, 4.5, 'python', (6+9j), True, False]
type(a)
<class 'list'>
b=6
type(b)
<class 'int'>
c=[6]
type(c)
<class 'list'>
#list[] methods
a=["python","java","c"]
a.append("c++")
a
['python', 'java', 'c', 'c++']
a.append("ML","AI")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a.append("ML","AI")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["ML","AI"])
a
['python', 'java', 'c', 'c++', ['ML', 'AI']]
#extend()
a.extend("HTML","CSS")
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.extend("HTML","CSS")
TypeError: list.extend() takes exactly one argument (2 given)
a.extend(["HTML","CSS"])
a
['python', 'java', 'c', 'c++', ['ML', 'AI'], 'HTML', 'CSS']
#insert()
a=["apple","banana","mango"]
a.insert(1,"kiwi")
a
['apple', 'kiwi', 'banana', 'mango']
#index()
a=["black","White","red","pink"]
a.index("White")
1
#copy()
a.copy()
['black', 'White', 'red', 'pink']
#You can use copy() to use the list elsewhere.
b=a.copy()
b
['black', 'White', 'red', 'pink']
a
['black', 'White', 'red', 'pink']
#sort()
a=["biryani","icecreams","chocolates"]
a.sort()
a
['biryani', 'chocolates', 'icecreams']
#for strings inside a list, sort does it aplhabetically.
b=[8,6,4,0,2,5]
b.sort()
b
[0, 2, 4, 5, 6, 8]
a=[7,9,"hello","python","animal",4,2,0]
a.sort()
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    a.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
b=[-8,-5,-2,0,-12,-1,-3]
b.sort()
b
[-12, -8, -5, -3, -2, -1, 0]
#reverse()
a=["ML","AI","DS","Python"]
a.reverse()
a
['Python', 'DS', 'AI', 'ML']
a.sort()
a
['AI', 'DS', 'ML', 'Python']
b=[4,5,6,9,10,2]
b.sort()
b
[2, 4, 5, 6, 9, 10]
b.reverse()
b
[10, 9, 6, 5, 4, 2]
#pop()
a=["HTML","CSS","JS"]
a.pop()
'JS'
a
['HTML', 'CSS']
a.pop("CSS")
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    a.pop("CSS")
TypeError: 'str' object cannot be interpreted as an integer
a.pop(1)
'CSS'
a
['HTML']
a=["hi","hello","how"]
del a
#remove()
a=["hi","hello","how"]
a.remove("hi")
a
['hello', 'how']
#len()
a="code"
len(a)
4
b=["code"]
len(b)
1
#count()
a=["sum","moon","star","sky"]
>>> a.count("star")
1
>>> a.append("moon")
>>> a.count("moon")
2
>>> b=["hello"]
>>> c=str(b)
>>> type(c)
<class 'str'>
>>> c.count("l")
2
>>> d=list(c)
>>> d
['[', "'", 'h', 'e', 'l', 'l', 'o', "'", ']']
>>> d.count("l")
2
>>> #clear()
>>> a=["water","drink"]
>>> a.clear()
>>> a
[]
>>> b=[]
>>> b.append("juice")
>>> b
['juice']
>>> #task
>>> a=[9,1,5,2,8,4,6,3,7,0]
>>> #output should be [7,6,4,3,0,9,8,5,2,1]
>>> a1=a[0:5]
>>> a1
[9, 1, 5, 2, 8]
>>> a2=a[5:]
>>> a2
[4, 6, 3, 7, 0]
>>> a1.sort()
>>> a1
[1, 2, 5, 8, 9]
>>> a1.reverse()
>>> a1
[9, 8, 5, 2, 1]
>>> a2.sort()
>>> a2.reverse()
>>> a2
[7, 6, 4, 3, 0]
>>> c=a2+a1
>>> a
[9, 1, 5, 2, 8, 4, 6, 3, 7, 0]
>>> c
[7, 6, 4, 3, 0, 9, 8, 5, 2, 1]
