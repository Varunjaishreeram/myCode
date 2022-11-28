# def getMatrixPath(r,c):
#     if r==1 and c==1:
#         return [""]
#     elif c==1:
#         return ["d"*(r-1)]
#     elif r==1:
#         return ["r"*(c-1)]

#     li=[]
#     rightStep=getMatrixPath(r,c-1)
#     leftStep=getMatrixPath(r-1,c)
#     for i in rightStep:
#         li.append("r"+i)
#     for j in leftStep:
#         li.append("d"+j)
#     return li


# print(getMatrixPath(2,3))

def printMazeMatrixPath(r,c,path):
    if c==1 and r==1:
        print(path)
        return
    elif c==0 or r==0:
        return



    printMazeMatrixPath(r,c-1,path+"r")
    printMazeMatrixPath(r-1,c,path+"d")


printMazeMatrixPath(3,5,"")




