Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def factorial(x):
	if x == 1:
		return 1
	return x*factorial(x-1)

>>> factorial(10)
3628800
>>> factorial(5)
120
>>> helf(print)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    helf(print)
NameError: name 'helf' is not defined
>>> help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

>>> value =5
>>> while value >0:
	print(value)
	value = value-1

	
5
4
3
2
1
>>> for n in [1,2,3,4,5,6,7,8,9]:
	print("-- {0} 단 --".format(n))
	for i in [1,2,3,4,5,6,7,8,9]:
		print("{0} * {1} = {2}".format(n, i, n*i))

		
-- 1 단 --
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5
1 * 6 = 6
1 * 7 = 7
1 * 8 = 8
1 * 9 = 9
-- 2 단 --
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
-- 3 단 --
3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 = 15
3 * 6 = 18
3 * 7 = 21
3 * 8 = 24
3 * 9 = 27
-- 4 단 --
4 * 1 = 4
4 * 2 = 8
4 * 3 = 12
4 * 4 = 16
4 * 5 = 20
4 * 6 = 24
4 * 7 = 28
4 * 8 = 32
4 * 9 = 36
-- 5 단 --
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
-- 6 단 --
6 * 1 = 6
6 * 2 = 12
6 * 3 = 18
6 * 4 = 24
6 * 5 = 30
6 * 6 = 36
6 * 7 = 42
6 * 8 = 48
6 * 9 = 54
-- 7 단 --
7 * 1 = 7
7 * 2 = 14
7 * 3 = 21
7 * 4 = 28
7 * 5 = 35
7 * 6 = 42
7 * 7 = 49
7 * 8 = 56
7 * 9 = 63
-- 8 단 --
8 * 1 = 8
8 * 2 = 16
8 * 3 = 24
8 * 4 = 32
8 * 5 = 40
8 * 6 = 48
8 * 7 = 56
8 * 8 = 64
8 * 9 = 72
-- 9 단 --
9 * 1 = 9
9 * 2 = 18
9 * 3 = 27
9 * 4 = 36
9 * 5 = 45
9 * 6 = 54
9 * 7 = 63
9 * 8 = 72
9 * 9 = 81
>>> L = [1,2,3,4,5,6,7,8,9]
>>> for I in L:
	if i>5:
		break
	print("item:{0}".format(i))

	
>>> for i in L:
	if i>5:
		break
	print("Item:{0}".format(i))

	
Item:1
Item:2
Item:3
Item:4
Item:5
>>> for i in L:
	if i%2 == 0:
		continue
	print("Item:{0}".format(i))

	
Item:1
Item:3
Item:5
Item:7
Item:9
>>> 
