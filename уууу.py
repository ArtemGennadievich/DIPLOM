# e = 'string'
# print(e[-3:6])
#
# for i in range(5):
#     if i % 2 == 0:
#         continue
#     print(i)
#
# n = 2.8956
# print(f'{n:.2f}')
#
# # for i in 'str':
# #     print(i.upper(), end='.')
#
# # a = [1, 2] - 1
# # print(a)
#
# c = [1, 2] + [0]
# print(c)
#
# import random
#
# print(random.uniform(1, 1.1))
#
# a = 1
# for i in range(1, 5):
#     a = a * i
#
# print(a)
#
# old_dict = {'a': 10, 'b': 10}
# new_dict = {}
# #
#
# for i, j in old_dict.items():
#     new_dict[j] = i
# print(new_dict)

# a = True
# #
# #
# def g():
#     a = None
#
#     def g2():
#         nonlocal a
#         a = 'py'
#
#     g2()
#
#
# g()
# print(a)

# for i in 'hello world':
#     if i == 'o':
#         break
#     print(i*2, end='')


# b = 'python'
# print(b[:6:2])
# num = float(2)

#
# class a:
#     def g(self):
#         print('rod class')
#
#
# class h(a):
#     def g(self):
#         print('doch class')
#
#
# hhh = h()
# hhh.g()
#
# while i:
#     print(i, break)


# c = lambda x: print(0)
# c(5)

# c = type({1: 2, 2: 1}) == type({1, 2})
# print(c)

# try:
#     a = 2 + '1'
#     print(a)
# except TypeError:
#     print('Error')

# for i in range(-2):
#     print(i)
#
# import time

# a = [1] + [1]
# print(a)
# a = set('hello')
# print(len(a))

# f = [1] * 2
# print(f)

# a = {'a': 10, 'c': 30}
# b = {'c': 20, 'e': 5}
#
# for i in a.keys():
#     if i not in b:
#         b[i] = a[i]
#
# print(b)


# try:
#     print(1)
# except Exception:
#     print(0)


# a = lambda x: x + x
# print(a(2))

# d = [1, 1, 2]
# print(len(set(d)))

# e = id({1}) == id({1})
# print(e)

# for i in range(1):
#     print(i)

# g = {'a': {'a': ['a']}}
# print(g.pop('a') == g.clear())

# d = lambda: False
# print(d())

# try:
#     b = 1/0
# except ZeroDivisionError:
#     b = 0
# print(b)

# import random
# print(2.1 == random.uniform(2.1,2.1))


# c = frozenset([1,2,3]) == {1,2,3}
# print(c)

#
# d = []
# if d:
#     print('hell')
# else:
#     print('it is')

# e = lambda x:x
# a = {1,2,3}
# b = e(a)
# print(a == b)


# x = 23
# num = 0 if x>10 else 11
# print(num)

# # private field = 0
# __field = 0

# for i in range(len('str')):
#     if i != 2:
#         print('str'[i], end='-')
#     else:
#         print('str'[1])


# c = 'some str'
# print(c[-3:9] + ' ' + c[0:5])

# d = {1, 2} == set([1, 2])
# print(d)

# import random
# print(random.random())

# def g(n):
#     if n == 0:
#         return 1
#     else:
#         return n * g(n-1)
#
# print(g(5))

# b = set('ppp')
# print(str(b) == 'p')
#
# dict = {{{'Socrat': 'Empty'}: {'Plato': 'A lot of material'}}: 'again'}
# key = {'Socrat': 'Empty'}
# print(dict[key]['Plato'])

# c = id([1]) == id([1.0])
# print(c)

# def y(a=2,b=3):
#     print(a+b)
#
# y(4)

# b = lambda x, y: print(y)
# b(1,2)

# t = (1,2,3)
# t2 = (4,5,6)
# t3 = t + t2
# print(t<t2)
# print(t2<t3)
# print(t<t3)

# s = map(lambda x: x * x, [0,1,2,3,4])
# print(list(s))

b = [1,2,3] + []
print(b)