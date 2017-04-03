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