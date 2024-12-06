unsorted = [6,5,3,1,3,8,7,2,4]

def sort(arr):
    for i in range(len(arr)):
        for j in  range(len(arr)):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
                print("swap")
                