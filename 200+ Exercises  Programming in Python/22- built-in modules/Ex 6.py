import re
raw_text = "Send an email to info@template.com or sales-info@template.it"

pattern = '[\w\.-]+@[\w\.-]+'

print(re.findall(pattern,raw_text))
