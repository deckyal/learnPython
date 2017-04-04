'''
Created on Apr 3, 2017

@author: deckyal
'''
class MyCalculator : 
    
    def addition(self,x,y):
        added = x + y;
        print(added);
        
    def substraction(self, x,y):
        sub = x-y;
        print(sub)
        
    def multiplication(self, x,y):
        mult = x*y;
        print mult;
        
        
    def division(self,x,y):
        div = x,y;
        print div;

c = MyCalculator();
c.addition(5,8)

def f1(self,x,y):
    return min(x,x+y)

class MyClass: 
    uy = f1;
    
    data = [];
    x = 2;
    def __init__(self):
        self.data = [1,2,3];
        self.data2 = [1,2,4];
        data2 = [2,3,5]
        print ("My class init")
        
class MyClass2(MyClass):
    def __init__(self): 
        print ("Class2 init");
        
        
test = MyClass2();
print(test.uy(5,4))