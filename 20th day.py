#
'''def my():
    name="python"
    print(name)
my()'''
# default argument
'''def my(n="python"):
    name=n
    print(name)
my()'''
#positional argument
'''def my(n):
    name=n
    print(name)
my("python")'''
#
'''def my(n,age):
    name=n
    print(name)
    print(age)
my("python",25)'''
#
'''def my(name,age):
    print(name,"my name")
    print(age,"my age")
my(25,name="AAA")'''
'''def my(name,age):
    print(name,"my name")
    print(age,"my age")
my(age=25,"AAA")'''
#keyword argument
'''def my(name="ABC",age=25,city="salem"):
    print(name,"my name")
    print(age,"my age")
    print(city)
my(name="new")'''

#add
'''def add(a,b):
    print(a+b)
add(5,7)'''
'''def mul(a,b):
    print(a*b)
mul(3,5)'''
'''def div(a,b):
    print(a/b)
div(12,6)'''
#or add
'''def add():
    a=int(input("enter the number:"))
    b=int(input("enter the number:"))
    print(a+b)
add()'''
#task
'''def clg(clg="XYZ",name="dharani"):
    print(clg," my clg")
    print(name,"my name")
def schl(name="abc"):
    print(name,"my name")
clg()
schl()'''
#arbitary argument
'''def new(*a):
    for i in a:
        print("it is my fab",i)
new("cookies")'''#tuple ah print agum
#keyword arbbitary
'''def new(**a):
    print(a)
new(name="abc",age=25)'''#dictionary ah print agum
#
'''def new(*a,**b):
    print(a," ")
    print(b," ")
new(5,6,7,8,9,name="A",age=25)'''
# both arbitary and keyword arbitary
'''def new(*a,**b):
    print(a," ")
    print(b," ")
new(5,6,7,8,9,name="A",age=25)'''
#task
'''def add(a,b):
    print(a+b)
def mul(a,b):
    print(a*b)
def sub(a,b):
    print(a-b)
def div(a,b):
    print(a/b)
while True:
    a=int(input("enter the no:"))
    if a==1:
        add(5,7)
    if a==2:
        mul(2,8)
    if a==3:
        sub(5,4)
    if a==4:
        div(65,2)
        break'''

'''def add(a,b):
    print(a+b)
def mul(a,b):
    print(a*b)
def sub(a,b):
    print(a-b)
def div(a,b):
    print(a/b)
while True:
    a=int(input("enter the no:"))
    b=int(input("enter the no:"))
    c=int(input("enter the no:"))
    if a==1:
        add(b,c)
    if a==2:
        mul(b,c)
    if a==3:
        sub(b,c)
    if a==4:
        div(b,c)
    break'''

 #
b=20
def my():
    a=10
    print(a)
my()
print(b)
    

