import re

content = '54aK54yr5oiR54R54ix5L2g'
content = re.sub('\d+', '', content)
print(content)
