#1. iterator
def fact(data):
    total=1
    for index in range(1,data):
        total=total*index
        yield total
        
for value in fact(5):  
    print(value) 

#2

class Length:
    def __len__(self):
        return 11
    def __str__(self):
        return "yamini"
    def __eq__(self,other): 
        return self is other 

obj = Length()
obj2=Length()
print(len(obj))
print(str(obj))
print(obj==obj2)
print(obj==obj)

#3.
from functools import wraps
import timeit

def Timeit(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = timeit.default_timer()
        print("Start Time:",start)
        result = f(*args, **kwargs)
        end = timeit.default_timer()
        print("End Time:",end)
        print('Elapsed time: {}'.format(end-start))
        return result
    return wrapper
@Timeit
def f(a):
    val=0
    for i in range(a):
        val=val+i
print(f(200000))
print(f(2000000))
