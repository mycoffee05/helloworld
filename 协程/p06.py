
# 斐波那契额数列的生成器写法
def fib(max):
    n, a, b = 0, 0, 1 # 注意写法
    while n < max:
        yield b
        a ,b = b, a+ b  # 注意写法
        n += 1

    # 需要注意，爆出异常是的返回值是return的返回值
    return 'Done'


g = fib(5)
'''
生成器典型用法是在for中使用
比较常用的典型生成器就是range
'''

for i in range(6):
    rst = next(g)
    print(rst)

ge = fib(10)
for i in ge:
    print(i)