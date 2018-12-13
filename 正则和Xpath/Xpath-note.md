# Xpath
- 在xml文件中查找信息的一套规则/语言,根据xml的元素或者属性进行遍历
- http://www.w3school.com.cn/xpath/index.asp # 官方文档
# Xpath 开发工具
- 开源的xpath表达式编辑工作：XMLQuire
- chrome插件：Xpath Helper
- Firefox插件：Xpath Checker
# 选取节点
- nodename:选取此节点的所有子节点
- /: 从根节点开始选取

            /Student:没有结果
            /School:选取节点
- //：选取节点，不考虑位置

        //age：选取三个节点，一般组成列表返回
        
- .:选取当前节点
- ..:选取当前节点的父亲节点
- @：选取属性
- xpath中查找 一般按照路径方法查找

       School/Teacher:返回Teacher节点    
       School/Student:返回Student list形式
       //Student：选取所有Student的节点，不考虑位置
       School//Age:选取School的后代中所有Age节点
       //@other:选取other属性
       //Age[@Detail]:Age元素下的属性Detail
       
# 谓语-Predicates
- /School/Student[1]:选取school下面第一个student节点
- /School/Student[last()]:最后一个
- /School/Student[last()-1]：倒数第二个                     
- /School/Student[position()<3] ：位置是第三个的Student节点
- //Student[@score]：属性Score节点
- //Student[@score=""99"]:选取属性score值为99的Student 节点

# XPath的一些操作
- |：或者

            //Student[@score] | //Teacher: 选取Student和Teacher的并集
            
- 其余不常见XPath运算符号：+-* div           