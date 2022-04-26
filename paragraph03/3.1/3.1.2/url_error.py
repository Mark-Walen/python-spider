# 处理异常
# 1.URLError
# URLError类来自urllib库的error模块，继承自OSError类，是error异常模块的基类
#   属性
#   * reason
# 2.HTTPError
# HTTPError类是URLError的子类，专门用来处理HTTP请求错误
#   属性
#   * code：返回HTTP状态码
#   * reason：同父类一样，用于返回错误的原因
#   * headers: 返回请求头.

from urllib import request, error

try:
    response = request.urlopen('https://cuiqingcai.com/index.htm')
except error.URLError as e:
    print(e.reason)
