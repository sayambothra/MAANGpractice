import re
pattern=re.compile(r"[A-Za-z0-9&@$%#]{8,}\d")
string="Champion1@"
a=pattern.search(string)
b=pattern.fullmatch(string)
print(a)
print(b)