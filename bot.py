from bs4 import BeautifulSoup
import urllib2
url=raw_input("Enter a website to extract the URL's from:")
r=urllib2.urlopen(url)
data=BeautifulSoup(r.read(),"html5lib").encode('utf-8')
soup=BeautifulSoup(data,"html5lib")
news=soup.find_all('div',class_="Normal")
ft=[]
for item in news:
    [s.extract() for s in item('div')]
    [s.extract() for s in item('br')]
    a=str(item.prettify()).split('\n')
    a=a[1:]
    a.pop()
    ft+=a
for item in ft:
    print item
