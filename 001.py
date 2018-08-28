#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module : Spider Doc'

__author__='HisenLee'  # add author

import urllib.request
# 读取百度的网页  timeout 单位是秒
file = urllib.request.urlopen("http://www.baidu.com", timeout=60)
htmlStr = file.read()
# wb以二进制格式写入  with语句会自动关闭流
with open("C:/Users/haixing/Desktop/baidu1.html", "wb") as output: 
	output.write(htmlStr)
# 第二种方式存取网页，直接urllib.request.urlretrieve，不用任何流，就可以完成读取网页，存到本地的操作
filename = urllib.request.urlretrieve("http://www.baidu.com", filename="C:/Users/haixing/Desktop/baidu2.html")
# 清除缓存
urllib.request.urlcleanup() 
# 获取网页信息
print(file.getcode()) #状态码200意味着正常获取成功
print(file.geturl()) # 获取url
# 对网页进行编码和解码
#urllib.request.quote("http://www.baidu.com")
#urllib.request.unquote("http://www.baidu.com")

# get请求 爬取出现403错误，说明禁止访问，需要爬虫修改报头来模拟浏览器进行访问
url = "http://www.baidu.com/s?wd="  # get请求 直接在url后拼接参数即可
key = "中文编码"
keyCode = urllib.request.quote(key)  # 对中文进行编码
urlAll = url + keyCode
req = urllib.request.Request(urlAll)
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0")
htmlStr = urllib.request.urlopen(req, timeout=60).read()
with open("C:/Users/haixing/Desktop/baidu3.html", "wb") as out: 
	out.write(htmlStr)
	
# post请求  [http://www.iqianyue.com/mypost 需求传入name, pass的字典格式]	
# 构建post请求需要看网页源代码的表单空间的name属性
import urllib.request
import urllib.parse 
url = "http://www.iqianyue.com/mypost/"
postData = urllib.parse.urlencode({"name":"allen", "pass":"123"}).encode("utf-8")   # 拼入post所需的data数据
req = urllib.request.Request(url, postData)
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0")
htmlStr = urllib.request.urlopen(req, timeout=60).read()
with open("C:/Users/haixing/Desktop/baidu3.html", "wb") as out: 
	out.write(htmlStr)
	
# http://www.xicidaili.com/ 西刺代理尽量找验证时间短的
def use_proxy(proxy_addr, url):   # 设置代理
	import urllib.request  
	proxy = urllib.request.ProxyHandler({'http':proxy_addr})
	opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
	urllib.request.install_opener(opener)
	data = urlllib.request.request.urlopen(url).read().decode("utf-8")
	return data

proxy_addr = "192.168.0.1:7777"	
data = use_proxy(proxy_addr, "http:www.baidu.com")
print(data)

# 开启debugLog (运行程序时打印log)
import urllib.request
httpHandler = urllib.request.HTTPHandler(debuglevel=1)
httpsHandler = urllib.request.HTTPSHandler(debuglevel=1)
opener = urllib.request.build_opener(httpHandler, httpsHandler)
urllib.request.install_opener(opener)
data = urlllib.request.request.urlopen(url).read().decode("utf-8")

# 爬虫经常遇到url相关的异常，使用URLError来处理
import urllib.request
import urllib.error
try:
	urllib.request.urlopen("http://www.baidu.com")
except urllib.error.URLError as e:
	if hasattr(e, "code"):	# 并不是所有的错误都有Errorcode，所以此处需要特殊判断是否有code属性
		print(e.code)
	if hasattr(e, "reason"):
		print(e.reason)
# 常见的状态码
# 200正常 304请求的资源未更新 400非法请求 403禁止访问 404未找到页面 500服务器内部错误

# 正则表达式
# 在python中，会使用re模块来实现正则
import re

pattern = "hello"
string = "http:www.hello.heecom"
result = re.search(pattern, string) # 从全文检索
result = re.match(pattern, string) # 从字符串开头开始匹配
pattern = re.compile("hello") # 对正则模式进行预编译
result = pattern.findall(string) # 会找出所有匹配的字符串，而不是只匹配一个
re.sub(pattern, rep, sourcestr, max) # 找出匹配的字符串用rep参数去替换源字符串中的匹配字段，替换max次
print(result)

# 通用字符
# \w 匹配任意一个字母，数字，下划线    \W 匹配除了字母，数字，下划线之外的任意一个字符
# \d 匹配任意一个十进制数字  \D 匹配除了十进制数字之外的任意一个字符
# \s 匹配任意一个空白字符  \S 匹配除了空白字符之外的任意一个字符

# 原子表 []表示
# [xyz] 匹配待x/y/z的任意一个即可    [^xyz] 匹配除了x/y/z之外的任意字符

# 任意匹配元字符 
# '.' 匹配除了换行符之外的任意一个字符

# 边界限制元字符
# ^ 匹配字符串开始 $ 匹配字符串结束
# ^abc 以abc开始的字符串   xyz$ 以xyz结束的字符串
# [^\s] ^符号如果放在[]中括号内的开头，则表示否定中口号里边的表达式，取相反即可

# 限定符 * + ? {n} {n,} {n,m}
# * 匹配前边的子表达式零次或多次 {0,}
# + 匹配前边的子表达式一次或多次 {1,}
# ？匹配前边的子表达式零次或一次 {0,1}
# {n} 匹配前边的子表达式n次, 连续出现n次
# {n,} 连续出现至少n次
# {n, m}出现次数在n-m之间都可以匹配

# 模式选择符 |
# 将多个表达式进行逻辑或运算，满足其一则结果就匹配

# 模式单元符 () 看做整体组合成大的原子
# (cd){1,}  cd至少出现一次  cd{1,} 表示d至少出现一次

# 模式修正符 I, M, L, U, S
# I 匹配时忽略大小写 M 多行匹配 L 做本地化识别匹配 U 根据Unicode解析字符 S 让.匹配包括换行符

# 贪婪模式和懒惰模式
# 贪婪模式就是 尽可能多的匹配； 懒惰模式就是 尽可能少的匹配
# 当?字符紧跟在任何一个其他限制符（*,+,?，{n}，{n,}，{n,m}）后面时，匹配模式是非贪婪的
# p.*y 默认是贪婪模式  在.*后添加? 就转化为懒惰模式 p.*?y 
# .[匹配除了\n和\r之外的任意单个字符]
# *[匹配前边的子表达式任意次{0,}]
# .*[表示任意个除了\n和\r之外的字符]
# .*?[表示任意个除了\n和\r之外的字符，尽可能少的匹配，懒惰模式]

# Cookie/Session
# 因为HTTP协议是无状态的，所有需要通过cookie/session来保存会话状态, cookie会把信息存在客户端，
# session会把信息存在服务器端

# 无cookie构建post请求
import urllib.request
import urllib.parse 
url = "http://www.iqianyue.com/mypost/"
postData = urllib.parse.urlencode({"name":"allen", "pass":"123"}).encode("utf-8")   # 拼入post所需的data数据
req = urllib.request.Request(url, postData)
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0")
htmlStr = urllib.request.urlopen(req, timeout=60).read()
with open("C:/Users/haixing/Desktop/baidu3.html", "wb") as out: 
	out.write(htmlStr)
	
	
# 导入cookie构建post请求
import urllib.request
import urllib.parse
import http.cookiejar # 处理cookie的包

url = "http://www.iqianyue.com/mypost/"
postData = urllib.parse.urlencode({"name":"allen", "pass":"123"}).encode("utf-8")   # 拼入post所需的data数据
req = urllib.request.Request(url, postData)
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0")
cjar = http.cookiejar.CookieJar() # 创建cookiejar对象
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar)) # 创建cookie处理器并构造opener
urllib.request.install_opener(opener) # 将opener安装为全局
htmlStr = urllib.request.urlopen(req, timeout=60).read()
with open("C:/Users/haixing/Desktop/baidu3.html", "wb") as out: 
	out.write(htmlStr)

	
	
