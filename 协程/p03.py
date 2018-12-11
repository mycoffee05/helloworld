# iter 函数实例
from collections import Iterator,Iterable
s = 'i love zhang'
print(isinstance(s,Iterable))
print(isinstance(s,Iterator))
s_iter = iter(s)
print(isinstance(s_iter,Iterator))
print(isinstance(s_iter,Iterable))