# search会返回第一个符号条件的目标
# findall()：返回匹配正则表达式的所有内容
# sub()：一串文本中想要去除的字符
# compile()：将正则字符串编译成正则表达式对象
import re

html = '''<li>
		<li data-view="4" class="active">
			<a href="/3.mp3" singer="齐秦">往事随风</a>
		</li>
	</li>
'''
result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
if result:
    print(result.group(1), result.group(2))
