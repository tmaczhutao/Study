import urllib.request
headers = {'X-Requested-With': 'XMLHttpRequest',
           'Referer': 'http://xueqiu.com/p/ZH010389',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0',
           'Host': 'xueqiu.com',
           #'Connection':'keep-alive',
           #'Accept':'*/*',
           "cookie": "aliyungf_tc=AQAAAHjiyiOjGAgASkaptEzLMgBJrzHx; device_id=47450bda487281063236eb48d547056d; remember=1; remember.sig=K4F3faYzmVuqC0iXIERCQf55g2Y; xq_a_token=caaf3b4278219ffb23157e84ba61bf0f6130aade; xq_a_token.sig=bZhzuM_7ROTSvO1XHaWg_eYEUsw; xq_r_token=f87a813a8f16dc1fcbba2c9812f79e2aed589308; xq_r_token.sig=m3u8BH1m0zhlOFLAyoZMJ_AMKZs; xq_is_login=1; xq_is_login.sig=J3LxgPVPUzbBg3Kee_PquUfih7Q; u=6987480589; u.sig=j40iJ8ou0iW4zXCzKceSUIDG6mE; s=gi19439jiy; bid=64dd61a714a90aee8a6f2b6b2723a595_j9qgbmw5; __utma=1.1593025798.1510109774.1510109774.1510116499.2; __utmb=1.3.10.1510116499; __utmc=1; __utmz=1.1510109774.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lvt_1db88642e346389874251b5a1eded6e3=1510107011; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1510116510"
           }
url = 'http://xueqiu.com/cubes/rebalancing/history.json?cube_symbol=ZH010389&count=20&page=1'
req = urllib.request.Request(url,headers=headers)
html = urllib.request.urlopen(req).read().decode('utf-8')
print(html)