def floodFill(r,c,dr,dc,arr,status):

    #print(r,c)

    if r==dr and c==dc:
        return [""]




    li=[]
    run=1
    for j in status:
        if (r-1,c)==j or (r+1,c)==j or (r,c+1)==j or (r,c-1)==j:
            run=0
            break

    if run==1:
        if r-1>=0 and r-1<=dr and c>=0 and c<=dc:
            if arr[r-1][c]!=1:
                status.append((r-1,c))
                print("up")
                li_up=floodFill(r-1,c,dr,dc,arr,status) #for going to up
                for i in li_up:
                    li.append("u"+i)
        if r+1>=0 and r+1<=dr and c>=0 and c<=dc:
            if arr[r+1][c]!=1:
                print("down")
                status.append((r+1,c))
                li_down=floodFill(r+1,c,dr,dc,arr,status) #for going to down
                for i in li_down:
                    li.append("d"+i)

        if r>=0 and r<=dr and c+1>=0 and c+1<=dc:
            if arr[r][c+1]!=1:
                status.append((r,c+1))
                print("right")
                li_right=floodFill(r,c+1,dr,dc,arr,status) #for going to right
                for i in li_right:
                    li.append("r"+i)
        if r>=0 and r<=dr and c-1>=0 and c-1<=dc:
            if arr[r][c-1]!=1:
                status.append((r,c-1))
                print("left")
                li_left=floodFill(r,c-1,dr,dc,arr,status) #for going to left
                for i in li_left:
                    li.append("l"+i)



    
    return li

status=[(0,0)]
arr=[[0,1,0,1],[0,0,1,0],[0,0,0,1],[1,0,0,0]]
print(floodFill(0,0,3,3,arr,status))

