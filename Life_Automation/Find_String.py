import re

phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
print(phoneNumRegex.findall("call me 415-545-1011 tomorrow, or at 415-555-9999"))