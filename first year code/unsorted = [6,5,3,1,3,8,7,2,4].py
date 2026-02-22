unsorted = [6,5,3,1,3,8,7,2,4]

def sort(arr):
    swaps = True
    while swaps:
        switch = 0
        for i in range(len(arr)):
            for j in  range(len(arr)):
                if arr[j] > arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]
                    switch +=1
            if switch ==  0 :
                swaps = False