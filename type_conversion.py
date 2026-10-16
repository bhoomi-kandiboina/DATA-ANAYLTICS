Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> int(10)
10
>>> int(9.0)
9
>>> int("hi")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    int("hi")
ValueError: invalid literal for int() with base 10: 'hi'
>>> int(6+8j)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int(6+8j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> int(True)
1
>>> int(False)
0
>>> float(10.8)
10.8
>>> float(34)
34.0
>>> float("good")
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    float("good")
ValueError: could not convert string to float: 'good'
>>> float(4+5j)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    float(4+5j)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> float(True)
1.0
float(False)
0.0
complex(3+9j)
(3+9j)
complex(9.8)
(9.8+0j)
complex(345)
(345+0j)
complex("do")
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    complex("do")
ValueError: complex() arg is a malformed string
complex(True)
(1+0j)
complex(False)
0j
str(2)
'2'
str(3.9)
'3.9'
str(9+5j)
'(9+5j)'
str("ride")
'ride'
str(True)
'True'
str(False)
'False'
bool(23)
True
bool(9.8)
True
bool(4+7j)
True
bool("forever")
True
bool(true)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    bool(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
bool(True)
True
bool(False)
False
