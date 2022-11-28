def findSubset(li, subset, target,i):
   
    
 
    if sum(subset) == target:
        print(subset,"answer")
        return
    if i==len(li) or sum(subset)>=target:
        return
        
    findSubset(li,subset,target,i+1)
    subset.append(li[i])
    findSubset(li,subset,target,i+1)
    subset.pop()

li = [10, 20, -10, 50, 40, 10]
target = 60
subset = []
level=0

findSubset(li, [], target,i=0)
