'''
Suppose a sorted array A is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array will not contain duplicates.

Note- Also think about the case when there are duplicates. Does your current solution work? How does the time complexity change?

PROBLEM APPROACH
Note: If you know the number of times the array is rotated, then this problem becomes trivial. If the number of rotation is x, then minimum element is A[x].
Lets look at how we can calculate the number of times the array is rotated.

No of rotataions = index of min element
'''

# *Approach 1*
# search foor the min value using linear search
def linearsearch(A):
    n=len(A)
    min_value=A[0]
    min_index=0
    for i in range(1,n):
        if A[i]<min_value:
            min_value=A[i]
            min_index=i
    return min_index
    
 #*Approach 2*
 def binarysearch(A):
    n=len(A)
    low,high=0,n-1
    while(low<=high):
        if A[low]<=A[high]:
            return A[low]
        mid=int((low+high)/2)
        nex=(mid+1)%n
        prev=(mid-1+n)%n
        if A[mid]<=A[nex] and A[mid]<=A[prev]:
            return A[mid]
        elif A[mid]<=A[high]:
            high=mid-1
        else:
            low=mid+1
    return -1
