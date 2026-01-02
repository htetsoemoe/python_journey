import re

text_h1 = "# Header 1"
h1_replacement = re.sub("^#\s(.*)", "<h1>\\1</h1>", text_h1)
print(h1_replacement)


text_bold = "This is **bold**. This is another **bold again**."
bold_replacement = re.sub("\*\*(.*?)\*\*","<b>\\1</b>",text_bold)
print(bold_replacement)

text_italic = "This is _italic_. This is another _italic again_."
italic_replacement = re.sub("_(.*?)_","<i>\\1</i>",text_italic)
print(italic_replacement)

