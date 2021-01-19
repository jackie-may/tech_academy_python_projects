


mySentence = 'loves the color'

color_list = ['red','blue','green','pink','teal','black']

def color_function(name):
    lst = []
    for i in color_list:# i is a temporary variable for the index of this list
        #inside the for loop
        msg = '{0} {1} {2}'.format(name,mySentence,i) #format combines the functions
        lst.append(msg)
    return lst




lst = color_function('Sally') #this has to be on the same indent as the 'def color_function()'
for i in lst:
    print(i)
