# 3.3 正则表达式
# 1.match
#   通用匹配
#    .*：其中.可以匹配任意字符(除换行符)，*代表匹配前面的字符无限次数
#   贪婪与非贪婪：
#       在贪婪匹配下，.*会匹配尽可能多的字符串
#       非贪婪匹配：.*?，如果匹配的结果在字符结尾，有可能匹配不到任何内容

import re

content = 'Hello 1234567 World_This is a Regex Demo'
print(len(content))
result = re.match('^Hello.*Demo$', content)
print(result)
print(result.group())
print(result.span())
