Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#striding
a="cloud computing"
a[::]
'cloud computing'
a[::1]
'cloud computing'
a[::3]
'cucpi'
a[3:9:1]
'ud com'
>>> a="Data Science"
>>> a[::4]
'D e'
>>> a[::2]
'Dt cec'
>>> a[::5]
'DSc'
>>> a[::8]
'De'
>>> a[1:8]
'ata Sci'
>>> a[5:]
'Science'
>>> a[3:9]
'a Scie'
>>> a[4:10]
' Scien'
>>> a="Python course"
>>> a[2:12:3]
'tnos'
>>> a[5:12:4]
'nu'
>>> a[1:11:5]
'y '
>>> a[0:9:2]
'Pto o'
>>> #negativestriding
>>> a="Machine Learning"
>>> a[-:-12:-4]
SyntaxError: invalid syntax
>>> a[-1:-2:-4]
'g'
>>> a[-1:-12:-4]
'gr '
>>> a[-2:-16:-5]
'nei'
>>> a[-4:-15:-2]
'naLeic'
>>> #toreverseastring
>>> a="Python course"
>>> a[::-1]
'esruoc nohtyP'
>>> #we cannot print if a>b in [a:b:c] for positive striding
>>> a[7:5:2]
''
>>> #we cannot print if a<b in [a:b:c] for negative striding
>>> a[-8:-4:-3]
''
