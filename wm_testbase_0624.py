��Python������ơ����п��Ծ����Լ�д�Ĵ𰸣��в���ȷ�ĵط������λ����ָ����������??????���ر�ע�ͣ�����ѡ���⣨ÿ��2�֣���24�֣�1�������ĸ���䣻A��x=y=z=1B��x=(y=z+1)��C��x,y=y,xD��x+=y��2������Python�ڴ��������˵��������ǣ���A������������������B�����������ȴ����͸�ֵ��ֱ��C����������ָ������D

��Python������ơ����п��Ծ�

���Լ�д�Ĵ𰸣��в���ȷ�ĵط������λ����ָ���� һ������⣨ÿ��1�֣���40�֣� 1��Pythonʹ�÷��ű�ʾע�ͣ�����һ��

���� ??? ??? ���ر�ע�͡� 2������ʹ��Python���ֽ�ɼ��У�������Ҳ����д��ͬһ�У����֮��Ҫ�� ; ���Ÿ����� 3��ÿһ��Python�ĵ���ģ��Ҫʹ�ùؼ��� import �� 4������Python 5��Python���������ͷ�Ϊ �������͡� 6��Python�������Ͱ��� Python��Ψһ��ӳ�����͡� 7��Python�ṩ������������ݱȽϲ����������������������Ƿ�ָ��ͬһ������Ҳ����ͨ���ڽ����������Զ������ݡ� 8��Python 9��Python�Ĵ�ͳ����������� �� 10����s=��abcdefg?����s[3]ֵ��s[3:5]ֵ�ǣ�s[:5]ֵ�ǣ�s[3:]ֵ��s[ : :2]ֵ�ǣ�s[::-1]ֵ��,s[-2:-5]ֵ�ǡ� 11��ɾ���ֵ��е�����Ԫ�صĺ����ǣ����Խ�һ���ֵ��������ӵ�����һ���ֵ��еĺ����� update(�ֵ�����) �����ذ����ֵ������м����б�ĺ����ǣ����ذ����ֵ�������ֵ���б�ĺ����ǣ��ж�һ�������ֵ����Ƿ���ڵĺ����� get() ��

����ѡ���⣨ÿ��2�֣���24�֣� 1�������ĸ������Python���ǷǷ��ģ� �� B ��

A��x = y = z = 1 B��x = (y = z + 1)

C��x, y = y, x D��x += y

2������Python�ڴ��������˵��������� ����

A������������������ B�����������ȴ����͸�ֵ��ֱ��ʹ��

C����������ָ������ D������ʹ��del�ͷ���Դ

3��������������ᵼ��Python��������ü������� �� ��

A�����󱻴��� B������Ϊ�������ݸ�����

C����Ϊ���������Ԫ�� D���ö����޷�����ʱ

4�������ĸ�����Python�Ϸ��ı�ʶ�� ��B��

A��int32 B��40XL C��self D��__name__

5����������˵���Ǵ���� ��A��

A�����ֵ������⣬���б�׼������������ڲ�������

B�����ַ����Ĳ���ֵ��False

C�����б����Ĳ���ֵ��False

D��ֵΪ0���κ����ֶ���Ĳ���ֵ��False

6�����б��ʽ��ֵΪTrue���� ��C��

A��5+4j > 2-3j B��3>2>2

C��(3,2)< (?a?,?b?) D��?abc? > ?xyz?

7��Python��֧�ֵ����������� ��A��

A��char B��int C��float D��list

8������Python�еĸ���������˵��������� ��B��

A����ʾ�������﷨��real + image j

B��ʵ�����鲿���Ǹ�����

C���鲿�����׺j���ұ�����Сд

D������conjugate���ظ����Ĺ����

9�������ַ�������˵��������� ��A��

A���ַ�Ӧ����Ϊ����Ϊ1���ַ���

B���ַ�����\0��־�ַ����Ľ���

C���ȿ����õ����ţ�Ҳ������˫���Ŵ����ַ���

D�����������ַ����п��԰������лس��������ַ�

10�����²��ܴ���һ���ֵ������� ��C��

A��dict1 = {} B��dict2 = { 3 : 5 }

C��dict3 = dict( [2 , 5] ,[ 3 , 4 ] )

D��dict4 = dict( ( [1,2],[3,4] ) )

11�����治�ܴ���һ�����ϵ������ ��C��

A��s1 = set () B��s2 = set (��abcd��)

C��s3 = (1, 2, 3, 4) D��s4 = frozenset( (3,2,1) )

12������Python�����ȷ���� ��D��

A��min = x if x < y else y B��max = x > y ? x : y

C��if (x > y) print x D��while True : pass

���������(ÿ��6�֣���36��)

1������һ������Python�ļ�Ӧ�����������Ľṹ��

2�������Python�������������ַ���s�Ƿ�Ϊ�Ϸ��ı�ʶ������������6���﷨�����������

void CheckId(string s): ����def CheckId(s):

alphas = 'abcdefghijklmnopqrstuvwxyz

ABCDEFGHIJKLMNOPQRSTUVWXYZ_' ������Ӧʹ��??? ???�� nums ="0123456789"

if ( len(s) > 1 )

firstChar = s[0]

if firstChar not in alphas:

print 'Error. First char must be alphas or number.'

else:

//ʹ����Ƭ������ȡ������1�ַ���������ַ�

otherChar = s(1 : ) ���� d[1:]

alphasnums = alphas + nums

while c in otherChar: ���� for

if c not in alphasnums:

print 'Error. Other chars must be alphas number or _ .' break

else:

print ("okay as an identifier") ������������

else:

if s not in alphas:

print 'Error.'

else:

print 'Okay as an identifier'

3��дһ������������һ�������������Ǹ���ĵڼ��졣 def getday(self,y=None,m=None,d=None):

date = datetime(y,m,d)

days = date.strftime('%j')

return days

4��дһ������������N������쳲��������е�N� def getn_vlaue(self,n):

if n<=2:

return 1

else:

return self.getn_vlaue(n-1)+self.getn_vlaue(n-2)

5����0��9�����ѡ������1��10�����������ɼ���A��ͬ�����ɼ���B�����A��B�Լ����ǵĲ����ͽ���

def getnumberlist(self):

a=[]

b=[]

j=k=0

for x in xrange(0,10):

j=int(random.random()*10) k=int(random.random()*10) a.append(j)

b.append(k)

print u'����a:',a

print u'����b:',b

return a,b

def getendlistj(self,a,b):#���� c = a+b

new_c = []

for x in xrange(0,len(c)): temp = c[x]

if temp not in new_c: new_c.append(temp)

print u'����:',new_c

def getendlistb(self,a,b):#���� new_a =[]

new_b = []
