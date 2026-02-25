#if-else condition by using comparison operators.
'''a=6
b=8
if a<b:
    print("Less")'''

'''a=6
b=8
if a>b:
    print("Less")
else:
    print("True")'''

'''a=6
b=8
if a<b:
    print("Less")
else:
    print("False")'''

'''a=3
b=9
if a!=b:
    print("NOt equal")
else:
    print("Equal")'''

'''a=3
b=9
if a==b:
    print("not equal")
else:
    print("Equal")'''

'''a=int(input())
b=int(input())
if a>b:
    print("greater")
else:
    print("False")'''

#if-else condition by using logical operators.

'''a=6
b=12
if a<b and b>a:
    print("True")
else:
    print("False")'''

'''a=3
b=7
if a!=b or a==b:
    print("Equal")
else:
    print("Not equal")'''
    
'''a=3
b=7
if not a!=b or a==b:
    print("Equal")
else:
    print("Not equal")'''

'''a=int(input())
b=int(input())
if a>=b and a<=b:
    print("Match")
else:
    print("Eliminate")'''

#if-else condition by using identify operators.

'''a="Away"
if type(a) is str:
    print("True")
else:
    print("False")'''

'''a="Also"
if type(a) is not int:
    print("Maybe true")
else:
    print("False")'''

'''a=int(input("Enter:"))
if type(a) is int:
    print("Wrong")
else:
    print("True")'''

#if-else condition by using membership operators.

'''a=[4,5,6,7,8,9,10]
b=int(input("A's value:"))
if b in a:
    print("Object found")
else:
    print("Try again!")'''

'''a=[4,5,6,7,8,9,10]
b=int(input("A's value:"))
if b not in a:
    print("Object not found")
else:
    print("Found")'''

#if-elif-else.
#if-elif-else condition by using comparison operators.

'''a=int(input("value of a:"))
b=int(input("value of b:"))
if a>b:
    print("1")
elif a<b:
    print("2")
elif a==b:
    print("3")
else:
    print("4")'''

'''a=8
b=12
if a==b:
    print("yes")
elif a!=b:
    print("Maybe")
else:
    print("No comment")'''

#if-elif-else condition by using logical operators.

'''a=int(input("a:"))
b=int(input("b:"))
if a>b and a>=b:
    print("a is maybe greater or both are equal.")
elif a<b and a<=b:
    print("a is maybe lesser or both are equal.")
elif a!=b or a==b:
    print("Maybe Equal or Not")
else:
    print("Can't determine!!")'''

#if-elif-else conition using membership operators.

'''a=[9,4,5,6,18,7]
b=int(input("Enter a value:"))
if b in a:
    print("Found")
elif b not in a:
    print("Not Found!")
else:
    print(" ")'''

#if-elif-else condition using identify operators.

'''a=input("Enter:")
if type(a) is str:
    print("valid")
elif type(a) is not str:
    print("Not valid")
else:
    print(" ")'''
    
