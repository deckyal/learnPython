'''
Created on Apr 3, 2017

@author: deckyal
'''

def example(): 
    return 15,12; #this is the tuple, no brackes and can't be modified. 

x,y = example();
print (x,y)

x = [1,3,5,6,2,1,6] #this is the list, like array we can modify it 
print (x);
print (x[0])

x.append(55)
print (x);

x.insert(2,33)
print(x)

x.remove(6)
print(x)

print(x[5])

print(x.index(1)) #to find the index

print(x.count(1)) #to count that number 

x.sort()
print(x)

y = ['Jan','Dan','Bob','Alice','Jack']
y.sort()
print(y)

y.reverse()
print(y)