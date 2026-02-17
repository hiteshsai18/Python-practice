Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #float()
>>> float(3)
3.0
>>> float(7.8)
7.8
>>> float("Hi")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    float("Hi")
ValueError: could not convert string to float: 'Hi'
>>> float(6+9j)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    float(6+9j)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> float(True)
1.0
>>> float(False)
0.0
>>> #In float; integer,float and boolean can be converted.
>>> #but not string and complex.
