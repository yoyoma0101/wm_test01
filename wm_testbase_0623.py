#coding='uft-8'

x=1
while x:
    x+=1
    print x
    #continue
    if x>=10:
       break
else:
    print 'end'


print 4,
print 5,
print 6,

f=open('print.txt','w')
print>>f,'wangmn and rongrong'
f.close()



