import re

boldregex = re.compile("<b>(.*?)</b>")
text = "<b>Hello World</b>! This is bold</b>"
match = boldregex.findall(text)
print(match)