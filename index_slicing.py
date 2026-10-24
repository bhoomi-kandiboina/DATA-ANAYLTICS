Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#indexing
a = 'Vijayawada'
a[1]
'i'
a[0]
'V'
a[9]+
SyntaxError: invalid syntax
a[9]+a[8]+a[7]
'ada'
a[0]+a[1]+a[2]+a[3]+
SyntaxError: invalid syntax
a[0]+a[1]+a[2]+a[3]+a[4]
'Vijay'
a = "i am in class"
a[1]+a[4]+a[7]
'   '
a[8]+a[9]
'cl'
a = i am learning python full stack
SyntaxError: invalid syntax
a = "i am learning python full stack"
a[15]+a[16]+a[17]+a[18]+a[19]
'ython'
a[14]+a[15]+a[16]+a[17]+a[18]+a[19]
'python'
a[5]+a[6]+a[7]+a[8]+a[9]
'learn'
a[2]+a[3]
'am'
a[20]+a[21]+a[22]+a[23]
' ful'
a[21]+a[22]+a[23]+a[24]
'full'

b = "Time is very precious"
a[14]+a[15]+a[16]+a[17]+a[18]+a[19]+a[20]
'python '
b[13]+b[14]+b[15]+b[16]+b[17]
'preci'
b[0]+b[1]+b[2]+b[3]
'Time'
b[7]+b[8]+b[9]+b[10]
' ver'
b[8]+b[9]+b[10]+b[11]
'very'

a="Vijayawada is a royal city'
SyntaxError: unterminated string literal (detected at line 1)
a = 'Vijayawada is a royal city'
a[-10]+a[-9]+a[-8]+a[-7]+a[-6]
'royal'
a[-4]+a[-3]+a[-2]+a[-1]
'city'
a[-15]+a[-14]
'is'

b="Vizag is a city of destiny"
b[-7]+b[-6]+b[-5]+b[-4]+b[-3]+b[-2]+b[-1]
'destiny'
b[-15]+b[-14]+b[-13]+b[-12]
'city'
b[-26]+b[-25]+b[-24]+b[-23]+b[-22]
'Vizag'


#Slicing

a="codegnan"
a[0:3]
'cod'
a[0:4]
'code'
a[4:8]
'gnan'
a[:4]
'code'
a[4:]
'gnan'

a = "work unti you succeed"
a="work until you succeed"
a[16:]
'ucceed'
a[15]
's'
a[15:]
'succeed'
a[13:18]
'u suc'
a[10:14]
' you'
a[5:10]
'until'
a[0:5]
'work '



b="simple is better than complex"
b[9:15]
' bette'
b[10:17]
'better '
b[10:16]
'better'
b[0:6]
'simple'
b[22:]
'complex'
b[7:9]
'is'

a="python is easy to learn"
a[-13:-9]
'easy'
a[-5:]
'learn'
a[:-17]
'python'

b="god is great"
b[-5:]
'great'
b[:-9]
'god'
b[-8:-10]
''
b[-8:-6]
'is'
b[-23:-17]
''
>>> a[-23:-17]
'python'
>>> b[-12:-9]
'god'
>>> 
>>> 
>>> 
>>> #striding
>>> a="Data Science"
>>> a[0:5:1]
'Data '
>>> a[0:5:2]
'Dt '
>>> a[0:4:2]
'Dt'
>>> a[::]
'Data Science'
>>> a[::2]
'Dt cec'
>>> a="cloud computing"
>>> a[::5]
'c u'
>>> a[::8]
'cm'
>>> a[3:11]
'ud compu'
>>> a[5:]
' computing'
>>> a[:12]
'cloud comput'
>>> a[::2]
'codcmuig'
>>> b="machine learning"
>>> b[1:9:2]
'ahn '
