import urllib.request
from  bs4 import BeautifulSoup

response = urllib.request.urlopen("file:///E:/Rushik/sem6/Python/RushikPython/collegeExercise/HtmlProgram/hello.html")
html1 = response.read()

soup = BeautifulSoup(html1,'html.parser')

for x in soup.find_all('td'):
    print(x.string)

print(soup.get_text())