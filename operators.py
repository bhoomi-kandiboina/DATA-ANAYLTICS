Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Operators
>>> #Arithmetic Operators
>>> a=4
>>> b=5
>>> a+b
9
>>> print(a-b)
-1
>>> print(a*b)
20
>>> print(a//b)
0
>>> print(a/b)
0.8
>>> print(a**b)
1024
>>> print(a%b)
4
>>> 
>>> #Assignment Operators
>>> a=6
>>> b=9
>>> print(a+=b)
SyntaxError: invalid syntax
>>> a+=b
>>> print(a)
15
>>> a-=b
>>> a
6
>>> a*=b
>>> a
54
>>> a/=b
a
6.0

#Comparision Operators
a=4
b=5
a<b
True
b>a
True
a<=b
True
b>=a
True
a!=b
True
a==b
False

#Logical Operators
a=5
b=7
a>b and b<a
False
a<b and b>a
True
a!=b
True
a!=b and a==b
False
a<b or b<a
True
a>b or b>a
True
a!=b or b==a
True
a<b or b>a
True
a not b
SyntaxError: invalid syntax
not TRUE
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    not TRUE
NameError: name 'TRUE' is not defined. Did you mean: 'True'?
not True
False
not False
True

#Identify Operators
a = 1,2,3,4,5,6,7,8,9
a=5
type (a) is int
True
type(a) is not int
False
a =5.6
type(a) is int
False
type(a) is float
True
type(a) is not float
False
b = 'ride'
type(b) is str
True
type(b) is not str
False
x = 3+7j
type(x) is complex
True
type(x) is not complex
False

#Membership Operators
a = 4,56,89,26,47
56 in a
True
78 ina
SyntaxError: invalid syntax
78 in a
False
78 not in a
True

#Bitwise Operators
a=3
b=4
a&b
0
a|b
7
a=5
b=6
a|b
7
a=7
~a
-8
-(a+1)
-8
a=-3
~a
2
a=7
b=8
a^b
15
a=5
b=7
a^b
2
a=7
a<<2
28
a=9
a<<4
144
a=8
a>>2
2
a=6
a>>3
0
