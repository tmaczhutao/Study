print("hash,", hash('abc'))
print("len,", len("aaaaa"))

print(globals())


def test():
    local_var = "1111"
    print(globals().get("local_var"))
    print(locals())


test()
print(globals().get("local_var"))
print("locals,", locals())
print("min,", min([1, 3, 4]))
print("max,", max([1, 3, 4]))
print("hex,", hex(15))

print("oct,", oct(8))

print("pow", pow(3, 2))

print(next(iter([21, 2])))

code = 'print(21)'
c = compile(code, '', 'exec')
print(c)

print("repr,", type(repr(c)))

print("round,", round(10.3345, 3))
# 切片
print("slice,", slice(2, 5))
d = range(10)
print(d)

for i in d[slice(2, 5)]:
    print(i)
print(d[slice(2, 5)])

c1 = sorted([2, 3, 521, 2, 45])
print(c1)
dic = {1: 5, 4: 2, 3: 4}
print(sorted(dic.items(), key=lambda x: x[1]))
print(sorted(dic.items()))

print("vars,", [x ** x for x in range(10)])

keys = [1, 2, 3, 4, 5]
values = ['a', 'b', 'c']
for i in zip(keys, values):
    print(i)

for i in map(lambda x, y: (x, y), keys, values):
    print(i)

c=map(None, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
print(type(c))

for i in iter(c):
    print(i)

