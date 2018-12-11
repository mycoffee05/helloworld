def SayHello(name):
    print('ss,{0}'.format(name))
    print('hello,{0}'.format(name))
    print('Done....')

if __name__ == '__main__':
    print('***'*10)
    name = input('plz input ur name:')
    print(SayHello(name=name))
    print('@@@'*10)
