import requests, bs4

result = requests.get("http://www.example.com")

# print(type(result))
# print(result.text)

# bs4 makes result.text easier to read
soup = bs4.BeautifulSoup(result.text,"lxml")
# print(soup)
print(soup.select('title'))
print(soup.select('title')[0].getText())

site_paragraphs = soup.select('p')
print(type(site_paragraphs))
print(type(site_paragraphs[0]))
print(site_paragraphs[0].getText())



