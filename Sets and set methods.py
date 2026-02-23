Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#sets{}
#sets is semi-mutrable(sometimes changeable and sometimes not).
a={3,5.6,"hitesh",5+9j,True,False}
print(a)
{False, True, (5+9j), 3, 5.6, 'hitesh'}
type(a)
<class 'set'>
b={7,9,5,6,7,9,3}
print(b)
{3, 5, 6, 7, 9}
type(b)
<class 'set'>
#set methods
#add
a={4,5,6,7,8,9}
a.add(20)
a
{4, 5, 6, 7, 8, 9, 20}
#issubset()
a={2,3,4,5,6,7}
b={5,6,7}
b.issubset(a)
True
a.issubset(b)
False
 a.issubset(a)
 
SyntaxError: unexpected indent
a.issubset(a)
True
#issuperset()
a={2,3,4,5,6,7,8,9}
b={2,3,4,5,6}
a.issuperset(b)
True
del a,b
a={1,2,3,5,6,7}
b={4,5,6}
a.issuperset(b)
False
#union()
a={3,4,5,6,7.8}
b={2,3,4,5,9}
a.union(b)
{2, 3, 4, 5, 6, 7.8, 9}
#intersection()
a={4,5,6,7,8,9}
b={6,7,8,9,10,11}
a.intersection(b)
{8, 9, 6, 7}
#difference()
a={2,3,4,5,6}
b={3,4,5,6,7,8}
a.difference(b)
{2}
b.ifferennce(a)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    b.ifferennce(a)
AttributeError: 'set' object has no attribute 'ifferennce'. Did you mean: 'difference'?
b.difference(a)
{8, 7}
#update()
a={10,11,12,13,14}
b={11,12,13,14,15}
a.update(b)
a
{10, 11, 12, 13, 14, 15}
b.update(a)
b
{10, 11, 12, 13, 14, 15}
#difference-update
a={4,5,6,7,8,9}
b={2,3,4,5,6,7,8,9,10}
a.difference_update(b)
a
set()
del a,b
a={2,3,4,5,6,7}
b={1,5,7,9,11,12}
a.difference_update(b)
a
{2, 3, 4, 6}
b.difference_update(a)
b
{1, 5, 7, 9, 11, 12}
#symmetric_difference
a={3,4,5,6,7,8,9}
b={1,2,3,8,9,10,11}
a.symmetric_difference(b)
{1, 2, 4, 5, 6, 7, 10, 11}
b.symmetric_difference(a)
{1, 2, 4, 5, 6, 7, 10, 11}
a
{3, 4, 5, 6, 7, 8, 9}
#symmetric_difference_update
a={1,3,5,7,9,11,13}
b={2,3,4,6,8,10,12}
a.symmetric_difference_update(b)
a
{1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
b.symmetric_difference_update(a)
b
{1, 3, 5, 7, 9, 11, 13}
a={7,8,9,10,11,12,13}
b={2,3,4,5,6,7,8,9}
a.interection_update(b)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    a.interection_update(b)
AttributeError: 'set' object has no attribute 'interection_update'. Did you mean: 'intersection_update'?
a.intersection_update(b)
a
{8, 9, 7}
b.interection_update(a)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    b.interection_update(a)
AttributeError: 'set' object has no attribute 'interection_update'. Did you mean: 'intersection_update'?
b.intersection_update(a)
b
{8, 9, 7}
#pop()
a={5,6,7,8,9,10}
a.pop()
5
a
{6, 7, 8, 9, 10}
a.pop(4)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    a.pop(4)
TypeError: set.pop() takes no arguments (1 given)
#remove()
a
{6, 7, 8, 9, 10}
a.remove(10)
>>> a
{6, 7, 8, 9}
>>> #copy
>>> a={3,4,5,6,7}
>>> a.copy()
{3, 4, 5, 6, 7}
>>> b=a.copy()
>>> b
{3, 4, 5, 6, 7}
>>> del a,b
>>> a={4,5,6,7,8}
>>> #clear()
>>> a.clear()
>>> a
set()
>>> b=a
>>> b.add(60)
>>> b
{60}
>>> #iscard()
>>> b.discard(60)
>>> b
set()
>>> #disjoint()
>>> a={3,4,5,6,7,8}
>>> b={2,4,5,6,7}
>>> a.isdisjoint(b)
False
>>> a={7,8,9}
>>> b={2,3,4}
>>> a.isisjoint(b)
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    a.isisjoint(b)
AttributeError: 'set' object has no attribute 'isisjoint'. Did you mean: 'isdisjoint'?
>>> a.isdisjoint(b)
True
>>> #len()
>>> a={5,6,7,8}
>>> len(a)
4
>>> #count()
>>> a.count(2)
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    a.count(2)
AttributeError: 'set' object has no attribute 'count'
>>> #no duplicate values, so no count method.
>>> #no order or sequence, so no index method.
