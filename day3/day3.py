#1 
nums = [1, 2, 3]
dict_comp = {num:num*num for num in nums}
print(dict_comp)
print(list(dict_comp.values()))  #values alone in a list
print(f"\n")


#2 set comprehension
nums=[1,2,5,2,3,1,4,5]
set_comp = {num*num for num in nums}
print(set_comp)
print(f"\n")


#3 
bank_details=[("Guido", 2000, 500), ("Raymond", -52, 1000), ("Jack", 900, 1000), ("Brandon", 2000, 0)]
proper_bal={row[0]:row[1] for row in bank_details if row[1]>=row[2]}
print(proper_bal) 

bal ={row[1] for row in bank_details}   
print(bal)

acc_holder=[row[0] for row in bank_details]
print(acc_holder)

proper_bal={row[0]:row[2]-row[1] for row in bank_details if row[1]<row[2]}
print(proper_bal)

non_zero_bal=[(row[0],row[1]) for row in bank_details if row[2]>0]
print(non_zero_bal)
print(f"\n")

#4
class Developer:
    def __init__(self):
        self.languages = []
        
    def resume(self):
        print(self.languages)
        
    def code(self,language):
        if language in self.languages:
            print(f"code in < {language} >")
        else:
            self.languages.append(language)
            

dev= Developer()
dev.code("python")
dev.code("java")
dev.code("python")
dev.resume()


class SrDeveloper(Developer):
    
    def __init__(self):
        self.reviews = []
        Developer.__init__(self)
        
    def review(self,review):           
        if(len(self.reviews)<len(self.languages)):
            self.reviews.append(review)
            print(self.reviews)
            
srdev=SrDeveloper()
srdev.review("Good")

class TechLead(SrDeveloper):
    
    def __init__(self):
        SrDeveloper.__init__(self)
    
    def design(self):
        print("design function in techlead class")
    
techlead=TechLead()
techlead.review("average")
techlead.design()
print(f"\n")

#5
import math
class Factorial:
    def fact(self,ele):
        return math.factorial(ele)
    
Fact=Factorial()
for index in range(1,6):
    print(index," ",Fact.fact(index))
print(f"\n")

        
#6
def modulecheck():
    print(__name__,"module works fine")
modulecheck()
if __name__ == '__main__':
    print("I'm running")



#7
string=input("Enter the string")

print("__str__ ",string.__str__())
print("__repr__ ",string.__repr__())
