# 1.模块 包含python代码的文件，后缀名是.py
- 好处：
    - 复用方便
    - 扩展方便
- 使用模块的目的
    - 为了程序维护方便，需要拆分
    - 模块可以增加代码重复利用的方式
    - 当作命名空间使用，避免命名冲突
- 如何定义模块
    - 模块就是一个普通.py文件,可以直接书写
    - 根据模块规范，最好在模块中编写以下内容
        - 函数（单一功能）
        - 类（相似功能的组合，或者类似业务模块
        - 测试代码
- 如何使用模块
    - 模块可以直接导入
    - 语法 参见包管理p001是模块,002是输出示例
          - 加入模块名称不能直接以数字开头，必须遵守python命名规则
          - 利用importlib实现以数字为开头的模块名称
    - 所谓模块导入，就是把模块内的代码全部粘贴到import位置，运行顺序也是import位置执行
        
        import module_name
        module_name.function_name
        module_name.class_name
    - 语法 import 模块 as 别名
        这样不用一直输入模块名称,导入的时候
    - from module_name import func_name,class_name
        - 选择性导入
        - 使用时候直接使用导入内容，不要模块名前缀
        - 案例003
    - from module_name import *
        - 省去模块前缀 
        - 示例p04
- if __name__ == '__main__'程序入口语句
    - 建议所有程序的入口都用这个代码
# 2.模块的搜索路径和存储
- 什么是搜索路径
    - 加载模块的时候，系统会在哪些地方寻找此模块
- 系统默认的模块搜索路径

        import sys
        sys.path 属性可以获取路径列表 
        案例p06.py
- 添加搜索路径

            sys.path.append(dir)

- 模块的加载顺序
    - 1. 搜索内存中已经加载好的模块
    - 2. python的内置模块
    - 3. 搜索sys.path的路径
   
# 包
- 包是一种组织管理代码的方式，包里面存放模块
- 用于将模块包含在一起的文件夹就是包
- 自定义包的结构

  |---包
  |---|--- __init__.py  包的标志文件
  |---|--- 模块1
  |---|--- 模块2
  |---|--- 子包(子文件夹)
  |---|---|--- __init__.py  包的标志文件
  |---|---|--- 子包模块1
  |---|---|--- 子包模块2
- 包的导入操作
    - import package_name
        - 直接导入一个包，可以使用__init__.py中的内容
        - 使用方式：
            
                package_name.func_name
                package_name.class_name.func_name()
        - 此种方式的访问内容是：
        - 案例pkg01,p07.py
    - import package_name as p
        - 具体用法跟作用方式，跟上述案例一致
        - 此种方法是默认对__init__.py内容的导入
    - import package.module
        - 导入包中某一个具体的模块
        - 使用方法
        
                package.module.func_name
                package.module.class.func()
                package.module.class.var
        - p08案例
    - import package.module as pm
    
- from ... import  导入
    - from package import module,module1,module2.....
    - 此种导入方法不执行‘__init__’的内容
    
            from pkg01 import p01
            p01.sayHello()
    - from package import *
        - 导入当前包‘__init__.py'文件中所有函数和类
        - 使用方法
        
                func_name()
                class_name.func_name()
                class_name.var
        - 案例 p09.py,注意导入的具体内容
- from package.module import *
    - 导入包中指定的模块的所有内容
    
            func_name()
            class_name.func_name()
            
- 在开发环境中会索引用其他模块，可以在当前包中直接导入其他模块的内容
    - import 完整路径
    
- ‘__all__'的用法
    - 在使用from package import *的时候，*可以导入的内容
    - '__init__.py'中如果文件为空，或者没有'__all__',那么只把'__init__'导入
    - '__init__'如果设置了'__all__',那么按照'__all__'指定子包或模块载入，不会载入其他内容
    - '__all__'=['module','module2']
    
# 命名空间
- 用于区分不用功能但相同名称的函数或者变量的特殊前缀
- 作用防止命名冲突

        setName()
        Student.setName()
        Dog.setName()