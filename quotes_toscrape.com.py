# Web Scraping Exercise. Site to scrape: www.toscrape.com

# TASK: Import any libraries you think you'll need to scrape a website.
import requests, bs4


# TASK: Use requests library and BeautifulSoup to connect to
# http://quotes.toscrape.com/ and get the HTML text from the homepage.
# res = requests.get('http://quotes.toscrape.com/')
# soup = bs4.BeautifulSoup(res.text, 'lxml')
# print(soup)


# TASK: Get the names of all the authors on the first page.
res = requests.get('http://quotes.toscrape.com/page/1/')
soup = bs4.BeautifulSoup(res.text, 'lxml')

authors = set()

for name in soup.select('.author'):
    authors.add(name.text)

print(authors)


# TASK: Create a list of all the quotes on the first page.

quotes = []

for quote in soup.select('.text'):
    quotes.append(quote.text)

print(quotes)


# TASK: Inspect the site and use Beautiful Soup to extract the top
# ten tags from the requests text shown on the top right from the
# home page (e.g. Love,Inspirational,Life, etc...).
# HINT: Keep in mind there are also tags underneath each quote,
# try to find a class only present in the top right tags, perhaps check the span.

top_tags = []

for tag in soup.select('.tag-item'):
    top_tags.append(tag.text)

print(top_tags)


# TASK: Notice how there is more than one page, and subsequent pages look like this
# http://quotes.toscrape.com/page/2/. Use what you know about for loops and string
# concatenation to loop through all the pages and get all the unique authors on the
# website. Keep in mind there are many ways to achieve this, also note that you will
# need to somehow figure out how to check that your loop is on the last page with quotes.
# For debugging purposes, I will let you know that there are only 10 pages, so the last
# page is http://quotes.toscrape.com/page/10/, but try to create a loop that is robust
# enough that it wouldn't matter to know the amount of pages beforehand, perhaps use
# try/except for this, it's up to you!

base_url = 'http://quotes.toscrape.com/page/{}/'

not_exceeded_pages = True
page = 1
all_authors = set()

while not_exceeded_pages:

    scrape_url = base_url.format(page)
    res = requests.get(scrape_url)

    if "No quotes found" in res.text:
        break

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    authors = soup.select('.author')

    for author in soup.select('.author'):
        all_authors.add(author.text)

    page += 1

print(all_authors)
