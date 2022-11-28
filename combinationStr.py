def combination(s):
    if len(s)==0:
        return [""]


    li2=[]
    for i in range(len(s)):
        c=s[i]
        tempStr=""
        for j in range(len(s)):
            if i==j:
                continue
            else:
                tempStr+=s[j]
        li1=combination(tempStr)
        for k in li1:
            li2.append(c+k)
    return li2


t=combination("abcd")
print(t,len(t))