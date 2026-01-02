import re

telenor = re.compile("(\+?95|0?9)7(9|8|7)\d{7}$")
if telenor.match("09791234567") == None :
    print("Not telenor")
else:
    print("telenor")

if telenor.match("09971234567") == None :
    print("Not telenor")
else:
    print("telenor")