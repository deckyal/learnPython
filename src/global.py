'''
Created on Apr 3, 2017

@author: deckyal
'''
x = 6;

def example2():
    global x;
    print(x)
    print(x+5)
    
    x += 6;
    
example2()