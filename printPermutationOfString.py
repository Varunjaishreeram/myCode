def printPermutationOfString(string,per):
    print(string)
    if string=="":
        print(per)
        return



    
    for i in range(len(string)):
        char=string[i]
        shorterString=""
        for j in range(len(string)):
            if j==i:
                continue
            else:
                shorterString+=string[j]
        printPermutationOfString(shorterString,per+char)


        

printPermutationOfString("abc","")