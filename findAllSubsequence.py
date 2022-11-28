def subsequence(s):
    if len(s)==0:
        return [""]


    firstChar=s[0]
    li1=[]
    li2=subsequence(s[1:]) 
    for i in li2:
     li1.append(i)
     li1.append(i+firstChar)

    return li1

print(subsequence("abc"))

c="a"
d=c[1:]
print(d,len(d))
