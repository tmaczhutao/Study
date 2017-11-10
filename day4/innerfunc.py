# 绝对值
print('abs', abs(-1))

print('all', all([1, 0]))
print('all', all([1, 1]))
print('all', all([]))

print('any', any([]))
print('any', any([1, 0]))
print('any', any([0, 0]))

print('ascii', ascii(['q']))
print('ascii', type(ascii(['q'])))

# ascii to char
print('chr', chr(1))
print('chr      %s' % chr(97))
# char to ascii
print('ord', ord('a'))

b = bytes('abcde', encoding='utf-8')
print("bytes", b)
print("bytes", b[0])

print("bytes", b.capitalize())
print("bytes", b)
b1 = bytearray('abcde', encoding='utf-8')
print("bytearray", b1)
print("bytearray", b1[1])
b1[2] = 105
print("bytearray", b1)

lambda1 = lambda n: n * n
print(lambda1(10))

array1 = [1, 2, 3]
for i in filter(lambda n: n > 1, array1):
    print(i)
code = '''array2=[1,2,3]
print(array2)
'''
c1 = compile(code, '', 'exec')
exec(c1);

res1 = map(lambda x: x ** x, range(11))
print(res1)
for i in res1:
    print("map,", i)

import functools

reduce = functools.reduce(lambda x, y: x + y, range(10))
print("reduce,", reduce)
