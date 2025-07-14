f =lambda:"Hello world!"
print(f())

x =lambda a:a+5
print(x(5))

x = lambda a,b:a*b
print(x(5,6))

x = lambda a,b,c:a+b+c
print(x(1,2,3))

numbers =[1,2,3,4,5]
squared =list(map(lambda x:x**2,numbers))
print(squared)

numbers = [1,2,3,4,5,6,7,8]
even_numbers =list(filter(lambda x:x%2==0,numbers))
print(even_numbers)

from functools import reduce
numbers =[1,2,3,4,5]
product =reduce(lambda x,y:x*y,numbers)
print(product)
