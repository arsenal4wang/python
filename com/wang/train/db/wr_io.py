import os

def writeTxt():
    o = open('test.txt','wb')
    i = 0
    while(i<10):
        o.write('hello world '+str(i)+'\n')
        i=i+1
    # o.write("hello world3")
    o.close()


def readTxt():
    o = open('test.txt','r+')
    # while(True):
    #   line = o.readline()
    #   if line:
    #       print '1'+"  " + line
    #   else:
    #       break
    for line in o:
       print  line.strip()
    o.close()

writeTxt()
readTxt()
