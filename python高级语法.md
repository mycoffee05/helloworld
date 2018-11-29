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