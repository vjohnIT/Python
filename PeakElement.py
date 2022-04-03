def findPeakUtil(arr,low,high,n) :

    mid = (high+low)//2

    if ((mid==0 or arr[mid-1] <= arr[mid])  and
     (mid ==n-1 or arr[mid+1] <= arr[mid])) :
        return mid
    
    elif (mid >0 and arr[mid-1] > arr[mid]) :
        return findPeakUtil(arr,low,mid-1,n)

    else :
        return findPeakUtil(arr,mid+1,high,n)





def findPeak(arr, n):

    return findPeakUtil(arr,0,n-1,n) 




# Driver Code

arr = [1,3,5,20,30,4,1,0]
n= len(arr)

print ("Index of the peak Element is ", findPeak(arr,n))