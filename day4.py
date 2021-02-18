#1
class Reverse:
    
    def __init__(self, data):
        self.data = data
        self.index = -2

    def __iter__(self):
        return self

    def __next__(self):
        try:
            if self.index + 2 >= len(self.data):
                raise StopIteration
            self.index = self.index + 2
            return self.data[self.index]
        except StopIteration:
            print("No more iteration possible")

rev = Reverse('hello')
it = iter(rev)
print(next(it))
print(next(it))
print(next(it))
print(next(it))


#2
import csv
with open('expr.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

with open('expr.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name",23])

with open('expr.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#4
import glob
for python in glob.iglob('**\*.py', recursive=True):
    print(python)


#5
import sys
print(f"Aguments: {list(sys.argv)}")

#6
import random
guess=random.randint(1,11)
num=int(input("Enter the number"))
count=1
while guess!=num :
    try:
        if(count==3):
            raise Exception
        if(num<guess):
            print("your guess value is lower than the real value")
            num=int(input("Enter the number"))
            count=count+1
        else:
            print("your guess value is higher than the real value")
            num=int(input("Enter the number"))
            count=count+1
    except Exception:
        print(f"You Lost\n\n")
        break
if(guess==num):
    print(f"you won\n\n")


#7 Value Error
import math
b=int(input("Enter the number"))
try:
    a=math.sqrt(b)
    print(a)
except ValueError:
    print("The value of b should be greater than 0")   # if b= -5

# Type Error
import math
b=input("Enter the number")
try:
    a=math.sqrt(b)
    print(a)
    
except TypeError:
    print("The Type of b should be integer")    #if b='e'


 #8.KeyError
details={"abcd":1,"def":2,"fgh":3}
try:
    print(details["abcd"])
    print(details["yamini"])
except:
    print("Enter the correct key")

#indexError
array=[1,2,3]
try:
    print(array[1])
    print(array[5])
except:
    print("Index out of bound")
