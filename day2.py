#1
import random
guess=random.randint(1,11)
num=int(input("Enter the number"))
count=1
while guess!=num and count<3:
    if(num<guess):
        print("your guess value is lower than the real value")
        num=int(input("Enter the number"))
        count=count+1
    else:
        print("your guess value is higher than the real value")
        num=int(input("Enter the number"))
        count=count+1
if guess==num:
    print(f"you won\n\n")
else:
    print(f"You lost\n\n")



#2
List=['a','b','c','d','e']
for index,value in enumerate(List):
    print(index,":",value,f"\n\n")


#3
directory={"name": "python", "ext": "py", "creator": "guido"}
for key,value in directory.items():
    print(value," belong to ",key)
print(f"\n\n")


#4
i=1
while i<=5:
    if i%2==0:
        print("even")
    else:
        print("odd")
    i+=1
else:
    print(f"Value of i is greater than 5\n\n")


#5

def add(a: int, b: int) -> int:
      """ give a and b as input...... 
....function returns sum of two values as output
"""
      return a+b
 
print(add.__doc__)
print(add(2,3))
print(type(add(2,3)),f"\n\n")



#6

def printvalue(*args):
    for i in args:
        print(i)

printvalue()
printvalue(2,3)
printvalue(1,2,3,4)
print(f"\n\n")


#7

def dictargs(**kwargs):
    print(len(kwargs))
dictargs()
dictargs(name='yamini')        
dictargs(name='yamini',age=21)
print(f"\n\n")


#8

def both(*args,**kwargs):
    print("args:",len(kwargs))
    print("kwargs:",len(args))

both()
both("yamini","23",name='yamini',age=21)
both(name='yamini')        
print(f"\n\n")


#9

a=[1,3,3,4,5,6]
lis= [i*i for i in a if i%2==1 ]
for i in lis:
    print(i)
print(f"\n\n")

#10
avg=lambda total,count:total/count
print(avg(30,5))
print(avg(5,2))
print(f"\n\n")



#11
lis = {'name': 'yamini', 'dateofbirth': '11-12-2004', 'age': 21}
lis2 = [key for key in lis.keys() if len(key)>=4]
print(lis2)
print(f"\n\n")


#12
matrix = [[1, 2, 3], [4,5,6], [7,8,9]]
#add 1 to all the elements
newmatrix=[ele+1 for list1 in matrix for ele in list1 ]
print(newmatrix)
print(f"\n\n")
