import sys

print(sys.getdefaultencoding())
s = "你好"
print(s,type(s))
s_to_utf=s.encode("utf-8")
print(s_to_utf)

s_to_unicode = s_to_utf.decode("utf-8")
print(s_to_unicode, type(s_to_unicode))
s_to_gbk =  s.encode("gbk")
print(s_to_gbk)
print(s_to_gbk.decode("gbk"))
