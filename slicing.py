Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #slicing
>>> a="codegnan"
>>> a[0:3]
'cod'
>>> a[0:4]
'code'
>>> a[4:8]
'gnan'
>>> a[:4]
'code'
>>> a[4:]
'gnan'
>>> a="simple is better than complex"
>>> a[10:16]
'better'
>>> a[22:29]
'complex'
>>> a[0:6]
'simple'
>>> a="beautiful is better than ugly"
>>> a[:9]
'beautiful'
>>> a[13:19]
'better'
>>> a[25:]
'ugly'
>>> #negativeslicing
>>> a="work hard until you succeed"
>>> a[-27:-23]
'work'
>>> a[-17:-12]
'until'
>>> a[-22:-18]
'hard'
>>> a[-11:-8]
'you'
>>> a[-7:]
'succeed'
>>> a="vijayawada is a royal city"
>>> a[-10:-5]
'royal'
>>> a[-26:-16]
'vijayawada'
>>> a[-4:]
'city'
>>> a[-7:0]
''
>>> a[-7:-1]+a[-1]
'al city'
