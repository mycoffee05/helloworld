# 结构化文件存储
- xml,json,
- 为了解决不同设备之间的信息交换问题
- xml
- json
# xml文件
- 参考资料
    - https://docs.python.org/3/library/xml.etree.elementtree.html
    - http://www.runoob.com/python/python-xml.html # 值得看一下
    - https://blog.csdn.net/seetheworld518/article/details/49535285
- 定义（）可扩展的标记语言
    - 标记语言：与严重使用尖括号括起来的文字字符串标记
    - 可扩展：用户可以自定义需要的标记
    - 例如
    
            <Teacher>
                自定义标记Teacher
                在两个标记之间任何内容都是与Teacher相关
            </Teacher>
    - w3c组织制定的一个标准
    - xml描述的是数据本身，即数据的结构和语言
    - html侧重于描述web页面数据，css侧重于页面本身，gs侧重于功能

- xml文档的构成
    - 处理命令
        - 只有一行，且必须在第一行
        - 内容是与xml本身处理相关的一些声明或者指令
        - 以xml关键字一般用于声明XML的版本和采用的编码
        - version属性是必须的
        - encoding属性用来支出xml解释器使用的编码开头      
    - 根元素(一个文件内只有一个根元素)
        - 在整个xml文件中，可以把他看成树形结构
        - 有且只有一个               
    - 子元素
    - 属性
    - 内容
        - 表明标签存储的信息
    - 注释
        - 说明作用的信息
        - 起说明规则，不能在标签内，只有在注释的开头和结尾用双短横线，三短横线只能出现在开头不能在结尾
            - <name> <!-- wangdapeng -->   </name> #可以
            - <name <!-- wangdapeng -->>   </name> #不可以，注释在标签内
  
            - <!--my-name-by-wang--> #可以，注释内容可以有一个短横线
            - <!--my--name--by--wang--> #不可以，双短横线只能出现在开头或结尾
  
            - <!---my-name--> #可以， 三短横线只能出现在开头
            - <!---my-name---> #不可以， 三短横线只能出现在开头
- 保留字符的处理
    - xml中使用的符号可能跟实际符号相冲突，典型的就是尖括号
    - 使用实体引用（EntityReferene) #转义
            
             - <score> score>80 </score> #有错误，xml中不能出现>
             - <score> score&gt;80</score> #使用实体引用       
    
    - 把含有保留字符的部分放在cdata块内部，cdata内部信息视为不需要转义
    
                  <![CDATA[
                     select name,age
                     from Student
                     where score>80
                    ]]>       
                    
                  字符串中的r'e'
- 常用的需要转移的保留字符和对应的实体引用                 
    - &:&amp;
    - <:&lt;
    - >:&gt;
    - ':&apos;
    - ":&quot;
    - 一共五个， 每个实体引用都以&开头并且以分号结尾
- XML标签的命名规则
    - Pascal命名法
    - 用单词表示，地一个字母大写
    - 区分大小写
    - 配对的标签必须一致    
- 命名空间
    - 为了防止命名冲突
        <Student>
              <Name>LiuYing</Name>
              <Age>23</Age>
        </Student>
        <Room>
          <Name>2014</Name>
          <Location>1-23-1</Location>
        </Room>
                
    - 如果归并上述两个内容信息，会产生冲突，为避免冲突，需在冲突，元素添加命名空间
        - xmlns:xml name space的缩写
        
      <Schooler xmlns:student="http://my_student" xmlns:room="http://my_room">
              <student:Name>LiuYing</student:Name>
              <Age>23</Age>
              <room:Name>2014</room:Name>
              <Location>1-23-1</Location>
      </Schooler>
      
# xml访问
## 读取
- XML读取两个主要技术，SAX,DOM
    - SAX (Simple API for XML):
        - 基于事件驱动触发
        - 利用SAX解析文档设计到解析器和事件处理两部分
        - 特点
            - 快
            - 流式读取

    - DOM
        - 是w3c规定的xml编程接口标准            
        - 原理：xml文件在缓存中以树形结构保存，读取
        - 用途
            - 增强查改
            - 定位浏览xml任何一个节点
        - minidom
            - minidom.parse(filename):加载读取的xml文件, filename也可以是xml代码
            - doc.documentElement:获取xml文档对象，一个xml文件只有一个对于的文档对象
            - node.getAttribute(attr_name):获取xml节点的属性值
            - node.getElementByTagName(tage_name)：得到一个节点对象集合
            - node.childNodes:得到所有孩子节点
            - node.childNodes[index].nodeValue:获取单个节点值
            - node.firstNode:得到第一个节点，等价于node.childNodes[0]
            - node.attributes[tage_name]
            - 案例P01
        - etree
            - 以树形结构来表示xml
            - root.getiterator:得到相应的可迭代的node集合
            - root.iter
            - find(node_name):查找指定node_name的节点,返回一个node
            - root.findall(node_name):返回多个node_name的节点
            - node.tag: node对应的tagename
            - node.text:node的文本值
            - node.attrib： 是node的属性的字典类型的内容
            - 案例P02
- xml文件写入
    - 更改
        - ele.set:修改属性
        - ele.append:添加子元素
        - ele.remove:删除子元素
        - 案例p03
    - 生成创建        
        - subElement,案例p04
        - minidom ,写入 p05
        - etree 写入 p06
       
            