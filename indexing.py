Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Indexing
#positiveindexing
a="vijayawada"
a[0]
'v'
a[2]
'j'
a[9]
'a'
a[0]+a[1]+a[2]+a[3]+a[4]
'vijay'
del a
a="i am in class"
a[0]
'i'
>>> a[1]
' '
>>> a[8]+a[9]+a[10]+a[11]+a[12]
'class'
>>> a[2]+a[3]
'am'
>>> a[1]
' '
>>> a[4]
' '
>>> a[7]
' '
>>> a[1]+a[4]+a[7]
'   '
>>> del a
>>> a="I love Python"
>>> a[2]+a[3]+a[4]+a[5]
'love'
>>> a[7]+a[8]+a[9]+a[10]+a[11]+a[12]
'Python'
>>> el a
SyntaxError: invalid syntax
>>> del a
>>> a="Time is very precious"
>>> a[0]+a[1]+a[2]+a[3]
'Time'
>>> a[8]+a[9]+a[10]+a[11]
'very'
>>> a[13]+a[14]+a[15]+a[16]+a[17]+a[18]
'precio'
>>> a[13]+a[14]+a[15]+a[16]+a[17]+a[18]+a[19]+a[20]
'precious'
>>> del a
>>> a="work hard"
>>> a[-9]+a[-8]+a[-7]+a[-6]
'work'
>>> a[-4]+a[-3]+a[-2]+a[-1]
'hard'
>>> del a
>>> a="i am learning python"
>>> a[-15]+a[-14]+a[-13]+a[-12]+a[-11]
'learn'
>>> a[-18]+a[-17]
'am'
>>> a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'python'
>>> del a
>>> #negativeindexing from a = "work hard"
