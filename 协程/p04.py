# 生成器使用
L = [x*x for x in range(5)] # 放在中括号内是列表生成器

g = (x*x for x in range(5)) # 放在小括号内是生成器

print(type(L))
print(type(g))