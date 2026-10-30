Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Sets
a = {3,6.7,"python",4+7j,True,False}
print(a)
{False, True, 'python', 3, 6.7, (4+7j)}
b={5,6,8,8,9,10,10}
print(b)
{5, 6, 8, 9, 10}

#methods
#add()
a = {4,5,6,7,8}
a.add(10)
a
{4, 5, 6, 7, 8, 10}
b={"see","to"}
a.add("you")
a
{'you', 4, 5, 6, 7, 8, 10}
b.add("you")
b
{'you', 'see', 'to'}

#issubset()
a={1,2,3,4,5,6}
b={4,5,6}
b.issubset(a)
True
a.issubset(b)
False

#issuperset()
a={1,2,3,4,5,6,7,8}
b={4,5,6,7}
a.issuperset(b)
True
b.issuperset(a)
False

#union()
a={1,3,4,5}
b={1,2,3,5,6,7,8}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8}

#intersection()
a={2,3,4,5,7,8,9}
b={4,5,6,3}
a.intersection(b)
{3, 4, 5}

#update()
a={4,5,6,7,8}
b={7,8,9,10,23}
a.update(b)
a
{4, 5, 6, 7, 8, 9, 10, 23}
b
{23, 7, 8, 9, 10}
b.update(a)
b
{4, 5, 6, 7, 8, 9, 10, 23}
a
{4, 5, 6, 7, 8, 9, 10, 23}

#difference()
a={3,4,5,6,7,8}
b={8,9,10,11,12,13}
a.difference(b)
{3, 4, 5, 6, 7}
b.difference(a)
{9, 10, 11, 12, 13}

c={1,2,3,4}
d={5,6,7,8}
a.difference(b)
{3, 4, 5, 6, 7}
c.difference(d)
{1, 2, 3, 4}
d.difference(c)
{8, 5, 6, 7}

#symmetric_difference()
a = {1,2,3,4,5,6}
b = {4,5,6,7,8,9}
a.symmetric_difference(b)
{1, 2, 3, 7, 8, 9}
b.symmetric_difference(a)
{1, 2, 3, 7, 8, 9}

#intersection_update()
a = {8,9,10,11,12,13}
b = {11,12 13,4,5,6}
SyntaxError: invalid syntax. Perhaps you forgot a comma?
b = {11,12,13,14,15}
a.intersection_update(b)
a
{11, 12, 13}
a
{11, 12, 13}
b.intersection_update(a)
b
{11, 12, 13}
b
{11, 12, 13}

#difference_update()
a = {10,20,30,40,50}
b = {30,40,50,60,70}
a.difference_update(b)
a
{20, 10}
b.difference_update(a)
b
{50, 70, 40, 60, 30}

#symmetric_difference_update()
a = {3,4,5,6,7,8,9}
b = {1,2,3,4,5,6}
a.symmetric_difference_update(b)
a
{1, 2, 7, 8, 9}
a
{1, 2, 7, 8, 9}
b.symmetric_difference_update(a)
b
{3, 4, 5, 6, 7, 8, 9}

#pop(),remove()
a = {2,3,4,5,6}
a.pop()
2
a.pop(2)
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    a.pop(2)
TypeError: set.pop() takes no arguments (1 given)
a.remove(4)
a
{3, 5, 6}
a.remove(2)
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    a.remove(2)
KeyError: 2
a.clear()
a
set()
a.discard(5)
a
set()
a.add(3)
a
{3}

#copy()
a={34,45,56,67}
a.copy()
{56, 34, 67, 45}
b.copy(a)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    b.copy(a)
TypeError: set.copy() takes no arguments (1 given)
b = a.copy()
b
{56, 34, 67, 45}
a.clear()
a
set()
b
{56, 34, 67, 45}
b.clear()
b
set()
>>> b.add(34)
>>> b
{34}
>>> b.add("ss")
>>> b
{34, 'ss'}
>>> 
>>> 
>>> #no index,count methods are allowed in set()
>>> a={5,6,7,8}
>>> a.index(5)
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    a.index(5)
AttributeError: 'set' object has no attribute 'index'
>>> a.count(5)
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    a.count(5)
AttributeError: 'set' object has no attribute 'count'
>>> 
>>> #length is common method
>>> len(a)
4
>>> 
>>> #isdisjoint()
>>> a = {4,5,6,7,8}
>>> b = {2,3,10,11}
>>> a.isdisjoint(b)
True
>>> a = {6,7,8,9}
>>> b = {7,8,9,2}
>>> a.isdisjoint(b)
False
