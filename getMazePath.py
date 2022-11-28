def getMazePath(n,path):
    if n==1:
        print(f"1{path},",end=" ")
        # print("1"+path,end=" ")
        return
    elif n==2:
        print(f"11{path},2{path}",end=" ")
        # print("11"+path,"2"+path,end=" ")
        return
    elif n==3:
        print(f"111{path},3{path},12{path},21{path}",end=" ")
        # print("111"+path,"3"+path,"12"+path,"21"+path,end=" ")
        return
    


    oneStep=getMazePath(n-1,path+"1")
    twoStep=getMazePath(n-2,path+"2")
    thirdStep=getMazePath(n-3,path+"3")
    

getMazePath(6,"")
