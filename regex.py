import re
text = "my email id is aarya@gmail.com"
pattern = r'\w+\@\w+\.\w+'
result = re.findall(pattern,text)
print(result)