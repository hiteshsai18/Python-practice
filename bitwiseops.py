Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #bitwise
>>> #&
>>> a=2
>>> b=4
>>> a&b
0
>>> bin(2)
'0b10'
>>> bin(4)
'0b100'
>>> a=3
>>> b=5
>>> a&b
1
>>> bin(3)
'0b11'
>>> bin(5)
'0b101'
>>> a=6
>>> b=8
>>> a&b
0
>>> a=3
>>> b=9
>>> a&b
1
>>> #|
>>> a=3
>>> b=5
>>> a
3
>>> a|b
7
>>> bin(3)
'0b11'
>>> bin(5)
'0b101'
>>> a=7
>>> b=8
>>> a|b
15
>>> bin(7)
'0b111'
>>> bin(8)
'0b1000'
>>> #~
>>> a=5
~a
-6
a=9
~a
-10
#^
a=2
b=4
a^b
6
bin(2)
'0b10'
bin(4)
'0b100'
#<<
a=2
a<<2
8
bin(2)
'0b10'
#>>
a=2
a>>2
0
a=5
a>>3
0
bin(5)
'0b101'
bin(8)
'0b1000'
bin(11)
'0b1011'
