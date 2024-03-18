import re

match = re.search(r'^\s.*[a-zA-Z]{5,30}\s.*$', input("Sender Name"))
if match:
    s_name = match.string.strip()
else:
    raise ValueError("Name must only contain alphabets between 5-30 c")

match = re.search(r'^\s.*[a-zA-Z]{5,60}\s.*$', input("Receiver name"))
if match:
    r_name = match.string.strip()
else:
    raise ValueError("Only Alphabets between 5-60 c allowed")


match = re.search(b'^ .*[^\\-\\.]{1}[a-zA-Z0-9\\-\\.]{1,62}[^\\-\\.]{1}@[a-zA-Z0-9\\-\\.]{1,247}\\.(com|net|org) .*$', input('Sender Email'))
if match:
    s_email = match.string.strip()
else:
    raise ValueError("Invalid email format")

match = re.search(b'^ .*[^\\-\\.]{1}[a-zA-Z0-9\\-\\.]{1,62}[^\\-\\.]{1}@[a-zA-Z0-9\\-\\.]{1,247}\\.(com|net|org) .*$', input('Receiver Email'))
if match:
    r_email = match.string.strip()
else:
    raise ValueError("Invalid email format")

html = ''
replacements = {}

for key, value in replacements:
    search = f'{key}'
    reg = '\\{'+search+'\\}'

    if re.search(reg, html):
        re.sub(reg, value, html)
    else:
        raise ValueError("Key not found in Html string")


if re.search("\\{.*\\}", html):
    raise ValueError("Html placeholder not found in replacements")