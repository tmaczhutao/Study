import urllib.request, urllib.parse, urllib.error
import http.cookiejar

LOGIN_URL = 'https://xueqiu.com/snowman/login'

values = {'remember_me': 'true', 'username': '13585685002', "password": "p987654321",
          "captcha": ""}  # , 'submit' : 'Login'
postdata = urllib.parse.urlencode(values).encode()
user_agent = r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
headers = {'User-Agent': user_agent, 'Connection': 'keep-alive'}

cookie_filename = 'cookie.txt'
cookie = http.cookiejar.MozillaCookieJar(cookie_filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)

request = urllib.request.Request(LOGIN_URL, postdata, headers)
try:
    response = opener.open(request)
    page = response.read().decode()
    #print(page)
except urllib.error.URLError as e:
    print(e.code, ':', e.reason)

cookie.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中
print(cookie)
# for item in cookie:
#     print('Name = ' + item.name)
#     print('Value = ' + item.value)

get_url = 'https://xueqiu.com/c'  # 利用cookie请求访问另一个网址
get_request = urllib.request.Request(get_url, headers=headers)
get_response = opener.open(get_request)
print(get_response.read().decode())
# print('You have not solved this problem' in get_response.read().decode())
