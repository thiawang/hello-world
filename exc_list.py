'''

@author: ewagyae
'''

list_1 = [i for i in range(1,101) if i%2==0 or i%3==0 or i%5 == 0]
for i in list_1:
    print '%s;'%i,