def test(b)
    if not isinstance(b,list)
        return
    prev_num=[0]
    temp=[prev_num]
    result=[]
    for x in b[1:]:
        if(x-int(prev_num))==1:
            temp.append(x)
        else;
            if len(temp)!=1:
                result.append(temp)
            temp=[x]
        prev_num=x
    result.append(temp)
    for j in result:
        print 'list length:%d'%len(j)
    print 'list count:%d' len(result)
    retuen result
    


a=[1,2,3,4,7,8,10,11,12]
print text(a)
input()
