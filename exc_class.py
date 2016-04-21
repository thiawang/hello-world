'''

@author: ewagyae
'''
class MyClass1:
    pass

class MyClass2:
    name = 'MyClass2'
    
    def sayHi(self):
        print 'Hello %s'%self.name

mc1 = MyClass1()
print 'mc1 is %s'%mc1

mc2 = MyClass2()
print 'mc2 is %s'%mc2
print mc2.name
mc2.name='Update%s'%mc2.name
print mc2.sayHi()
