'''
  Given a sorted array of integers, find the number of occurrences of a given target value.
  Your algorithm’s runtime complexity must be in the order of O(log n).
  If the target is not found in the array, return 0

  **Example : **
  Given [5, 7, 7, 8, 8, 10] and target value 8,
  return 2.
'''

# **Approach 1**
def find_count(Arr,n,x):
    count=0
    for i in range(0,n):
        if Arr[i]==x:
            count+=1
        elif Arr[i]>x:
            break
    return count
  
# **Approach 2**
def find_count(Arr,n,x):
    #set stating and ending index
    start, end = 0, n-1
    count=0
    while start <= end :
        mid = int((start + end) / 2)
        # we found a match
        if Arr[mid] == x :
            dest = mid
            break
        # go on right side
        elif Arr[mid] < x :
            start = mid + 1
        # go on left side
        else :
            end = mid - 1
    if(start>end):
        return 0
    else:
        #check the nearby locations
        for i in range(dest,-1,-1):
            if Arr[i]==x:
                count+=1
            else:
                break
        for i in range(dest+1,n):
            if Arr[i]==x:
                count+=1
        return count  
        
# **Approach 3**
def findCount(self, A, x):
    def BinarySearch(Arr,n,x,searchFirst):
        low,high=0,n-1
        result=-1
        while(low<=high):
            mid=int((low+high)/2)
            if Arr[mid]==x:
                result=mid
                if(searchFirst==0):
                    high=mid-1 #go on searching towards left(lower indices)
                else:
                    low=mid+1 #go on searching towards right(higher indices)
            elif Arr[mid]>x:
                high=mid-1
            else:
                low=mid+1
        return result
    n=len(A)
    FirstIndex=BinarySearch(A,n,x,0)
    if(FirstIndex==-1):
        return 0
    else:
        LastIndex=BinarySearch(A,n,x,1)
        return LastIndex-FirstIndex+1 
