Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #complex
>>> complex(2)
(2+0j)
>>> complex(6.7)
(6.7+0j)
>>> complex("Python")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    complex("Python")
ValueError: complex() arg is a malformed string
>>> complex(5+6j)
(5+6j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> #only string cannot be converted in complex type conversion.
