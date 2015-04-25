#!/usr/bin/python
# coding=utf-8
import urllib2
import urllib
import cookielib
import re
import getpass

auth_url = 'http://zccx.tyb.njupt.edu.cn'
home_url = 'http://zccx.tyb.njupt.edu.cn/student'
def input():
    stuid = raw_input('请输入学号:')
    password = raw_input('请输入姓名:')
    return [stuid,password]
def chaxun(stuid,password):
    data = {
        'authenticityToken': '',
        'number': stuid,
        'name': password
    }
    # urllib进行编码

    txt = urllib2.urlopen(auth_url)
    # 解析页面查找authenticityToken的值
    txt = txt.read()
    p = re.compile('name=\"authenticityToken\" value=\"[^\"]*')
    p = p.findall(txt)
    p = str(p[0])
    s = p.split('value=\"')
    data['authenticityToken']=s[1]
    post_data = urllib.urlencode(data)
    # 发送头信息
    headers = {
        "Host": "zccx.tyb.njupt.edu.cn",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:36.0) Gecko/20100101 Firefox/36.0",
        "Referer": "http://zccx.tyb.njupt.edu.cn/?",
        "Origin": "http://zccx.tyb.njupt.edu.cn",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    # 初始化一个CookieJar来处理Cookie
    cookieJar = cookielib.CookieJar()
    # 实例化一个全局opener
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
    # 获取cookie
    req = urllib2.Request(home_url, post_data, headers)
    result = opener.open(req)
    #print result.read()
    txt = result.read()#.decode('gb2312')
    return txt;

[stuid , password]=input()
txt = chaxun(stuid,password)
s = 'form action=\"/student\" method=\"post\" accept-charset=\"utf-8\" enctype=\"application/x-www-form-urlencoded\"'
# 访问主页 自动带着cookie信息
while s in txt:
    print '似乎有些不太对，不妨再输一次学号姓名？'
    [stuid ,password]=input()
    txt=chaxun(stuid,password)
#获取晨跑次数
p = re.compile('<span class=\"badge\">[^<]*')
x = p.findall(txt);
x = str(x[0])
x = x.split('>');
print password+'这学期的晨跑次数为'+x[1]+'次'
