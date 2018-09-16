Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Person:
	Name = "Default Name"
	def Print(self):
		print("My Name is {0}".format(self.Name))

		
>>> p1 = Person()
>>> p1.Print()
My Name is Default Name
>>> isinstance(p1,Person)
True
>>> class MyClass:
	def __init__(self,value):
		self.Value = value
		print("Class is created! Value = ",value)

		
>>> class MyClass:
	def __del__(self):
		print("Class is deleted!")

		
>>> def foo():
	d = MyClass(10)

	
>>> foo()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    foo()
  File "<pyshell#19>", line 2, in foo
    d = MyClass(10)
TypeError: MyClass() takes no arguments
>>> class HousePark:
	lastname = "고"
	def __init__(self,name):
		self.fullname = self.lastname + name
	def travel(self,where):
		print("%s, %s여행을 가다."%(self.fullname, where))

	
>>> travel()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    travel()
NameError: name 'travel' is not defined
>>> 
