# 1.Robots协议
# Robots协议也称作爬虫协议、机器人协议，它的全名叫做网络爬虫排除标准。
# robots.txt样例
#   User-agent:*
#   Disallow:/
#   Allow:/public/
# 3.robotsparser
#   常用方法
#   set_url()：用来设置robots.txt文件的链接
#   read()：读取robots.txt文件并进行分析。注意，这个方法执行一个读取和分析的操作，
#   如果不调用这个方法，接下来的判断都为False。
#   parse()：用来解析robots.txt文件，传入的参数是robots.txt某行的内容，它会按照
#   robots.txt的语法规则来分析这些内容。
#   can_fetch()：该方法传入两个参数，第一个是User-agent，第二个是要抓取的URL。
#   返回的内容是搜索引擎是否可以抓取这个URL，返回是True或False
#   mtime()：返回的是上次抓取和分析robots.txt的时间
#   modified()：将当前时间设置为上次抓取和分析robots.txt的时间。

from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
rp.set_url('http://www.jianshu.com/robots.txt')
rp.read()
print(rp.can_fetch('*', 'http://www.jianshu.com/p/b675554025d7d'))
print(rp.can_fetch('*', 'http://www.jianshu.com/search?q=python&page=1&type=collecctions'))
