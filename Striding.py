Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a = "python course"
>>> a[-2:-10:-3]
'son'
>>> a[-3:-13:-4]
'r t'
>>> a[-1:-12:-6]
'e '
>>> a[-4:-9:-2]
'ucn'
>>> a[9:5:2]
''
>>> #In positive striding highest to lowest not possible
>>> 
>>> a[-10:-4:-3]
''
>>> #In negative striding lowest to highest not possible
>>> 
>>> a[::1]
'python course'
>>> a[::-1] # without using reverse string
'esruoc nohtyp'
