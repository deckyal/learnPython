'''
Created on Apr 3, 2017

@author: deckyal
'''

def example():
    print('this code will run')
    z = 3 + 9
    print(z)
    
example()

def simple_addition(num1,num2) :
    answer = num1+num2;
    return answer;

data = simple_addition(5, 3)

data2 = simple_addition(num2 =5,num1 = 3)
print data
print data2

def simple(num1,num2=2):
    print num1;
    print num2;
    pass

simple(1,3)