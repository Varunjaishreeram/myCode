def knightTour(chess,row,col,count,s):
    
    # print("varun",count)
    # print(count)
    if row<0 or col<0 or row>4 or col>4 or chess[row][col]==1:
        return
    elif count==25:
        print(s)
        return
    



    
    # print(row,col,count)
    tempRow=[-2,-1,1,2,-2,-1,1,2]
    tempCol=[1,2,2,1,-1,-2,-2,-1]
    chess[row][col]=1
    for i in range(8):
        
        knightTour(chess,row+tempRow[i],col+tempCol[i],count+1,s+f"{row+tempRow[i]}-{col+tempCol[i]},")
    chess[row][col]=0






chess=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
row,col=2,3
knightTour(chess,row,col,1,"")
print("hello")
