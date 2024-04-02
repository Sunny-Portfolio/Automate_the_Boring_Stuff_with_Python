import re

regex = re.compile(r'\d{3}-\d{3}-\d{4}')
result = regex.search('this is : 123-456-7890')
print(result.group())
print(result.group(0))

regex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
result = regex.search('this is : 123-456-7890')
print(result.group())
print(result.group(0))
print(result.group(1))
print(result.group(2))

print('-----------')
result = regex.findall('this is : 444-444-4444')
print(result)


re.compile(r'^[A-Z][a-z]+\sWatanabe')