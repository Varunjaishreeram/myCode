def nQueen(n,status,currentRow,li,bigLi):
    if currentRow==n:
        t=li[:]
        bigLi.append(t)
        return

    for i in range(n):
        if check(n,currentRow,i,status):
            status[currentRow][i]=1
            temp=""
            for j in range(n):
                if j==i:
                    temp+="Q"
                else:
                    temp+="."
            li.append(temp)
            nQueen(n,status,currentRow+1,li,bigLi)
            status[currentRow][i]=0
            li.pop()
    
    
    return bigLi

        
def check(n,row,col,status):
    tempRow,tempCol=row,col
    while tempRow>=0:
        if status[tempRow][tempCol]==1:
            return False
        tempRow-=1
    tempRow,tempCol=row,col
    while tempRow>=0 and tempCol>=0:
        if status[tempRow][tempCol]==1:
            return False
        tempRow-=1
        tempCol-=1
    tempRow,tempCol=row,col
    while tempRow>=0 and tempCol<n:
        if status[tempRow][tempCol]==1:
            return False
        tempRow-=1
        tempCol+=1
    return True



n=1
bigLi=[]
status=[[0]*n for i in range(n)]
x=nQueen(n,status,0,[],bigLi)
print(x)