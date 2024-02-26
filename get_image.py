import requests, bs4

result = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')

soup = bs4.BeautifulSoup(result.text, "lxml")
computer = soup.select('.mw-file-element')[1]
print(computer['src'])

# Download image to local directory
image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg')

f = open('my_computer_image.jpg', 'wb')
f.write(image_link.content)
f.close()



