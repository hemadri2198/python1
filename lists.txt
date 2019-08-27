Python 3.7.3 (default, Apr  3 2019, 05:39:12) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=[1,2,"hello",6,4,3,-10,3.4]
>>> a[0]
1
>>> a[0:6]
[1, 2, 'hello', 6, 4, 3]
>>> a[-1]
3.4
>>> a[-2]
-10
>>> a[4:-2]
[4, 3]
>>> len(a)
8
>>> a.insert(3,"students")
>>> a
[1, 2, 'hello', 'students', 6, 4, 3, -10, 3.4]
>>> a.remove("hello")
>>> a
[1, 2, 'students', 6, 4, 3, -10, 3.4]
>>> a.pop()
3.4
>>> a.pop(4)
4
>>> a
[1, 2, 'students', 6, 3, -10]
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> a=(4,6,7]
SyntaxError: invalid syntax
>>> a=[4,6,7]
>>> a.clear()
>>> a
[]
>>> x=[3,5,[4.4,"hi"]]
>>> x
[3, 5, [4.4, 'hi']]
>>> a=[4,55,2,33,7.6,-90]
>>> a.sort()
>>> a
[-90, 2, 4, 7.6, 33, 55]
>>> a.reverse()
>>> a
[55, 33, 7.6, 4, 2, -90]
>>> a=["a","b","a"]
>>> a.count("a")
2
>>> 
