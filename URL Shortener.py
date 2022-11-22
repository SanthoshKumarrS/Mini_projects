import pyshorteners

link = 'https://www.edx.org/course/analyzing-data-with-excel'

shortener1 = pyshorteners.Shortener()
Shortened_link = (shortener1.tinyurl.short(link))

print(Shortened_link)

