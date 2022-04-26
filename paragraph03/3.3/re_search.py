import re

content = 'Extra strings Hello 1234567 World This is a Regex Demo Extra strings'
# result = re.match('Hello.*?(\d+).*?Demo', content)
result = re.search('Hello.*?(\d+).*?Demo', content)
print(result)
