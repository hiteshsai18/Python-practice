Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #int
>>> #int()
>>> int(7)
7
>>> int(7.8)
7
>>> int("Hitesh")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("Hitesh")
ValueError: invalid literal for int() with base 10: 'Hitesh'
>>> int(7+9j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(7+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> int(True)
1
>>> int(False)
0
>>> #only integer, float and boolean converts in integer.
>>> #string and complex cannot convert.
