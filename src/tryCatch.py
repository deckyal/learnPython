'''
Created on Apr 4, 2017

@author: deckyal
'''
import csv;

with open('example.csv') as csvfile: 
    readCSV = csv.reader(csvfile, delimiter = ',')
    dates = []
    colors = []
    for row in readCSV: 
        color = row[3]
        date = row[0]
        
        dates.append(date)
        colors.append(color)
        
    print(dates)
    print(colors)
    
    
    try: 
        whatColor = input('What color : ')
        
        if whatColor in colors : 
            
            coldex = colors.index(whatColor)
            theDate = dates[coldex]
            print('The date of ',whatColor,'is ',theDate)
            
        else : 
            print ('The color is not found ')
        
    except Exception as e: 
        print(e)
        
    print('Still running though.. ')