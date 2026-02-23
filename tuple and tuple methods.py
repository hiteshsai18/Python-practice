Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #tuple()
>>> #tuple is immutable(cannot manipulate it)
>>> a=(3,6.7,"hi",6+5j,True, False)
>>> print(a)
(3, 6.7, 'hi', (6+5j), True, False)
>>> type(a)
<class 'tuple'>
>>> #tuplemethods
>>> #index()
>>> a.index("hi")
2
>>> #len()
>>> len(a)
6
>>> #count()
>>> a.count(True)
1
