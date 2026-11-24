def binary_Search(arr,target):
    l=0
    r=len(arr)-1

    while l<=r:
        mid =(l+r) // 2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            r=mid-1
        else:
            l=mid+1

print(binary_Search([1,2,3,4,5,6,7,8,9],7))


    