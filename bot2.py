from bs4 import BeautifulSoup
import urllib2
url=raw_input("Enter a website to extract the URL's from:")
r=urllib2.urlopen(url)
data=BeautifulSoup(r.read(),"html5lib").encode('utf-8')
soup=BeautifulSoup(data,"html5lib")
news=soup.find_all('div',class_="ins_storybody")
ft=[]
a=str(soup.html.title.prettify()).split("\n")
a=a[1:]
a.pop()
a.pop()
ft+=a
for item in news:
    [s.extract() for s in item('div')]
    [s.extract() for s in item('br')]
    [s.extract() for s in item('b')]
    [s.extract() for s in item('p')]
    a=str(item.prettify().encode('utf-8')).split('\n')
    a=a[1:]
    a.pop()
    ft+=a
print "Heading:",
for item in ft:
    print item
