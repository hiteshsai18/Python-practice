Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a={"name":"Hitesh","city":"Eluru","Mailid":"Hitesh@gmail.com"}
>>> a.get("city")
'Eluru'
>>> b=a.copy()
>>> b
{'name': 'Hitesh', 'city': 'Eluru', 'Mailid': 'Hitesh@gmail.com'}
>>> a
{'name': 'Hitesh', 'city': 'Eluru', 'Mailid': 'Hitesh@gmail.com'}
>>> a.clear()
>>> a
{}
>>> b
{'name': 'Hitesh', 'city': 'Eluru', 'Mailid': 'Hitesh@gmail.com'}
>>> b.update({"mobile no":9027392733})
>>> b
{'name': 'Hitesh', 'city': 'Eluru', 'Mailid': 'Hitesh@gmail.com', 'mobile no': 9027392733}
>>> #there are no index and count in dictionary.
>>> #if you print a dict, it will remove duplicate values.
>>> a={"idnos":[10,20,30],"names":["a","b","c"],"places":["vja","hyd","vzg"]}
>>> print
<built-in function print>
>>> 

>>> print(a)
{'idnos': [10, 20, 30], 'names': ['a', 'b', 'c'], 'places': ['vja', 'hyd', 'vzg']}
>>> a.keys()
dict_keys(['idnos', 'names', 'places'])
>>> a.values()
dict_values([[10, 20, 30], ['a', 'b', 'c'], ['vja', 'hyd', 'vzg']])
>>> a.items()
dict_items([('idnos', [10, 20, 30]), ('names', ['a', 'b', 'c']), ('places', ['vja', 'hyd', 'vzg'])])
