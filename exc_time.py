'''
@author: ewagyae
'''
import time  
starttime = time.time()
print 'start:%f' % starttime
for i in range(10):
    time.sleep(1)
    print i
endtime = time.time()  
print 'end:%f' % endtime
print 'total time:%f' % (endtime-starttime) 