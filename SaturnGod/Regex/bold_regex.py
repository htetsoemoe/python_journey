import re

boldregex = re.compile(".*<b>(.*)</b>.*")
text = "Hello <b>Wrold</b>"
match = boldregex.match(text)

print(map)
print(match.group(0))
print(match.group(1))