import urllib
import urllib2

from bs4 import BeautifulSoup

#
# url = "http://www.packtpub.com/books"
# page = urllib2.urlopen(url)
# soup_packtpage = BeautifulSoup(page)

helloworld = "<p>Hello World</p>"


#soup_string = BeautifulSoup(helloworld)
#print(soup_string)
# print  soup_packtpage




html_tag = """<html><body><p>Test html a tag example</p>
<a href="##" target="_blank">Home</a>
<a href='#'>Books</a>
</body>
</html> """

soup = BeautifulSoup(html_tag)
atag = soup.a

print(atag.attrs)
