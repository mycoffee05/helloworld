# 生成一个生成器 函数案例
def odd():
    print('step 1')
    print('step 2')
    print('step 3')
    return None
odd()
print('*'*8)
# 改写生成器
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 2
    print('step 3')
    yield 3
    return None

g = odd()
one = next(g)  # next调用生成器
print(one)
# g实例化生成器
two = next(g)
print(two)
#
three = next(g)
print(three)