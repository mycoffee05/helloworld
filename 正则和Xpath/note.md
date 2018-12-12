# Xpath
- 在xml文件中查找信息的一套规则/语言,根据xml的元素或者属性进行遍历
- http://www.w3school.com.cn/xpath/index.asp
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