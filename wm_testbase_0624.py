《Python程序设计》期中考试卷；（自己写的答案，有不正确的地方还请给位批评指正）；叫做??????的特别注释；二、选择题（每题2分，共24分）1．下列哪个语句；A、x=y=z=1B、x=(y=z+1)；C、x,y=y,xD、x+=y；2．关于Python内存管理，下列说法错误的是（；A、变量不必事先声明B、变量无须先创建和赋值而直；C、变量无须指定类型D

《Python程序设计》期中考试卷

（自己写的答案，有不正确的地方还请给位批评指正） 一、填空题（每空1分，共40分） 1．Python使用符号标示注释；还有一种

叫做 ??? ??? 的特别注释。 2．可以使用Python语句分解成几行；多个语句也可以写在同一行，语句之间要用 ; 符号隔开。 3、每一个Python的导入模块要使用关键字 import 。 4、所有Python 5、Python的数字类型分为 等子类型。 6、Python序列类型包括 Python中唯一的映射类型。 7、Python提供了两个对象身份比较操作符和来测试两个变量是否指向同一个对象，也可以通过内建函数来测试对象的身份。 8、Python 9、Python的传统除法运算符是 。 10、设s=‘abcdefg?，则s[3]值是s[3:5]值是，s[:5]值是，s[3:]值是s[ : :2]值是，s[::-1]值是,s[-2:-5]值是。 11、删除字典中的所有元素的函数是，可以将一个字典的内容添加到另外一个字典中的函数是 update(字典名称) ，返回包含字典中所有键的列表的函数是，返回包含字典中所有值的列表的函数是，判断一个键在字典中是否存在的函数是 get() 。

二、选择题（每题2分，共24分） 1．下列哪个语句在Python中是非法的？ （ B ）

A、x = y = z = 1 B、x = (y = z + 1)

C、x, y = y, x D、x += y

2．关于Python内存管理，下列说法错误的是 （）

A、变量不必事先声明 B、变量无须先创建和赋值而直接使用

C、变量无须指定类型 D、可以使用del释放资源

3、下列哪种情况会导致Python对象的引用计数增加 （ ）

A、对象被创建 B、被作为参数传递给函数

C、成为容器对象的元素 D、该对象无法访问时

4、下面哪个不是Python合法的标识符 （B）

A、int32 B、40XL C、self D、__name__

5、下列哪种说法是错误的 （A）

A、除字典类型外，所有标准对象均可以用于布尔测试

B、空字符串的布尔值是False

C、空列表对象的布尔值是False

D、值为0的任何数字对象的布尔值是False

6、下列表达式的值为True的是 （C）

A、5+4j > 2-3j B、3>2>2

C、(3,2)< (?a?,?b?) D、?abc? > ?xyz?

7、Python不支持的数据类型有 （A）

A、char B、int C、float D、list

8、关于Python中的复数，下列说法错误的是 （B）

A、表示复数的语法是real + image j

B、实部和虚部都是浮点数

C、虚部必须后缀j，且必须是小写

D、方法conjugate返回复数的共轭复数

9、关于字符串下列说法错误的是 （A）

A、字符应该视为长度为1的字符串

B、字符串以\0标志字符串的结束

C、既可以用单引号，也可以用双引号创建字符串

D、在三引号字符串中可以包含换行回车等特殊字符

10、以下不能创建一个字典的语句是 （C）

A、dict1 = {} B、dict2 = { 3 : 5 }

C、dict3 = dict( [2 , 5] ,[ 3 , 4 ] )

D、dict4 = dict( ( [1,2],[3,4] ) )

11、下面不能创建一个集合的语句是 （C）

A、s1 = set () B、s2 = set (“abcd”)

C、s3 = (1, 2, 3, 4) D、s4 = frozenset( (3,2,1) )

12、下列Python语句正确的是 （D）

A、min = x if x < y else y B、max = x > y ? x : y

C、if (x > y) print x D、while True : pass

三、简答题(每题6分，共36分)

1、简述一个典型Python文件应当具有怎样的结构？

2、下面的Python函数检查给定的字符串s是否为合法的标识符，程序中有6处语法错误，请改正：

void CheckId(string s): 改正def CheckId(s):

alphas = 'abcdefghijklmnopqrstuvwxyz

ABCDEFGHIJKLMNOPQRSTUVWXYZ_' （改正应使用??? ???） nums ="0123456789"

if ( len(s) > 1 )

firstChar = s[0]

if firstChar not in alphas:

print 'Error. First char must be alphas or number.'

else:

//使用切片操作，取出除第1字符外的其它字符

otherChar = s(1 : ) 改正 d[1:]

alphasnums = alphas + nums

while c in otherChar: 改正 for

if c not in alphasnums:

print 'Error. Other chars must be alphas number or _ .' break

else:

print ("okay as an identifier") 改正缩进不对

else:

if s not in alphas:

print 'Error.'

else:

print 'Okay as an identifier'

3、写一个函数，计算一个给定的日期是该年的第几天。 def getday(self,y=None,m=None,d=None):

date = datetime(y,m,d)

days = date.strftime('%j')

return days

4、写一个函数，给定N，返回斐波那契数列第N项。 def getn_vlaue(self,n):

if n<=2:

return 1

else:

return self.getn_vlaue(n-1)+self.getn_vlaue(n-2)

5、从0到9中随机选择，生成1到10个随机数，组成集合A，同理生成集合B，输出A和B以及它们的并集和交集

def getnumberlist(self):

a=[]

b=[]

j=k=0

for x in xrange(0,10):

j=int(random.random()*10) k=int(random.random()*10) a.append(j)

b.append(k)

print u'集合a:',a

print u'集合b:',b

return a,b

def getendlistj(self,a,b):#并集 c = a+b

new_c = []

for x in xrange(0,len(c)): temp = c[x]

if temp not in new_c: new_c.append(temp)

print u'并集:',new_c

def getendlistb(self,a,b):#交集 new_a =[]

new_b = []
