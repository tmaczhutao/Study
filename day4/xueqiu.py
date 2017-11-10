url = "https://xueqiu.com/stock/f10/bizunittrdinfo.json?date=20171107&_=1510116531938"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0',
    'Host': 'xueqiu.com',


    "Referer": "https://xueqiu.com/hq",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
    "cookie":"aliyungf_tc=AQAAAHjiyiOjGAgASkaptEzLMgBJrzHx; device_id=47450bda487281063236eb48d547056d; remember=1; remember.sig=K4F3faYzmVuqC0iXIERCQf55g2Y; xq_a_token=caaf3b4278219ffb23157e84ba61bf0f6130aade; xq_a_token.sig=bZhzuM_7ROTSvO1XHaWg_eYEUsw; xq_r_token=f87a813a8f16dc1fcbba2c9812f79e2aed589308; xq_r_token.sig=m3u8BH1m0zhlOFLAyoZMJ_AMKZs; xq_is_login=1; xq_is_login.sig=J3LxgPVPUzbBg3Kee_PquUfih7Q; u=6987480589; u.sig=j40iJ8ou0iW4zXCzKceSUIDG6mE; s=gi19439jiy; bid=64dd61a714a90aee8a6f2b6b2723a595_j9qgbmw5; __utma=1.1593025798.1510109774.1510109774.1510116499.2; __utmb=1.3.10.1510116499; __utmc=1; __utmz=1.1510109774.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lvt_1db88642e346389874251b5a1eded6e3=1510107011; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1510116510"
}
import urllib.request
import json
import http.cookiejar

baidu=urllib.request.urlopen("https://www.baidu.com")
print(baidu.read())
req = urllib.request.Request(url, headers=headers)
print(req)
html = urllib.request.urlopen(req).read().decode('utf-8')

print(html)
js = json.loads(html)
print(js)
print(type(js))
