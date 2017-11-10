# 生成式
c = [i * 2 for i in range(10)]
print(c)

import time

print(time.time())
time.sleep(3)
# 生成器
d = (i * 3 for i in range(10))
print(d)


import urllib.request

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

html = getHtml("http://tieba.baidu.com/p/2738151262")

print (html)


#装饰器模式
def log(func):
    print("start.............")
    def wapper(*args, **kwargs):
        start_time = time.time();
        print(args, kwargs)
        res = func(*args, **kwargs)
        end_time = time.time();
        print("times ,", end_time - start_time)
        return res;

    return wapper


@log
def t(ab, a):
    time.sleep(1)
    print(ab, a)



#装饰器模式
def logs(type):

    print("start.............")
    def wapper_out(func):
        print(type)
        def wapper(*args, **kwargs):
            start_time = time.time();
            print(args, kwargs)
            res = func(*args, **kwargs)
            end_time = time.time();
            print("times ,", end_time - start_time)
            return res;
        return  wapper
    return wapper_out

print("--------------------------------")
@logs(type="333")
def t1(ab, a):
    time.sleep(1)
    print(ab, a)
t1("bbb", "1")








