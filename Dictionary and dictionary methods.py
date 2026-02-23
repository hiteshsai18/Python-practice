Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dict()
a={"name":"Hitesh","year":"2026","month":"Feb"}
print(a)
{'name': 'Hitesh', 'year': '2026', 'month': 'Feb'}
a.keys()
dict_keys(['name', 'year', 'month'])
a.values()
dict_values(['Hitesh', '2026', 'Feb'])
>>> a.items()
dict_items([('name', 'Hitesh'), ('year', '2026'), ('month', 'Feb')])
>>> #accessing
>>> a={"year":2026,"date":20}
>>> a["year"]
2026
>>> a[2026]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a[2026]
KeyError: 2026
>>> #update
>>> a.update({"mailid":"hitesh@gmail.com"})
>>> a
{'year': 2026, 'date': 20, 'mailid': 'hitesh@gmail.com'}
>>> a.update({"month":"Feb","Day":"Sunday"})
>>> a
{'year': 2026, 'date': 20, 'mailid': 'hitesh@gmail.com', 'month': 'Feb', 'Day': 'Sunday'}
>>> #setdefault
>>> a={"time" :6,"hour":1,"sec":2}
>>> a.setdeault("date",20)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.setdeault("date",20)
AttributeError: 'dict' object has no attribute 'setdeault'. Did you mean: 'setdefault'?
>>> a.setdefault("date",20)
20
>>> a
{'time': 6, 'hour': 1, 'sec': 2, 'date': 20}
>>> #pop
>>> a={"colour":"blue","food" : "biryani"}
>>> a.pop()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
>>> a.pop("colour")
'blue'
>>> a
{'food': 'biryani'}
>>> a.update({"colour":"blue"})
>>> a
{'food': 'biryani', 'colour': 'blue'}
>>> a.popitem()
('colour', 'blue')
>>> a
{'food': 'biryani'}
