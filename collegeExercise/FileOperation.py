'''
    file Operations Exercise
'''
'''
#write Mode
f = open('sample.txt','w')
f.write('Hello')
f.close()

#Append Mode
f = open('sample.txt',"a")
f.write(" world ")
f.close()

#Read Mode
f = open('sample.txt','r')
print(f.read())
f.close()
'''

'''
    urlopen
'''
from urllib.request import urlopen
html = urlopen("http://localhost/feedback")
print(html.read())



