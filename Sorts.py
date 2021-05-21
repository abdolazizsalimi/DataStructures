
def heapfy(arr , n ,i ):

    #parentroot 
    largestroot = i 
    left = 2 * i + 1
    right = 2 * i +2 
    if left < n and arr[largestroot] < arr[left]:
        largestroot = left  
    if right < n and arr[largestroot] < arr[right]:
        largestroot = right
    if largestroot != i : 
        arr[i],arr[largestroot]= arr[largestroot],arr[i]
        heapfy(arr, n , largestroot)
    
    
def heapSort (arr):
    size = len(arr)
    for i in range(size//2 -1 , -1 ,-1):
        arr[i], arr[0] = arr[0], arr[i]
        heapfy(arr , i , 0 )

print()
arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print("Sorted array by heapSort ")
print(arr)




def merge_towo_sorted_arry(a,b):
    sorted_list = []
    i = j = 0 
    len_a = len(a)
    len_b = len(b) 
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i+=1 
        else : 
            sorted_list.append(b[j])
            j+=1
    while i < len_a:
        sorted_list.append(a[i])
        i+=1         
    while j < len_b:
        sorted_list.append(b[j])
        j+=1

    return sorted_list

def magreSort(arry):
    if len(arry)<=1:
        return arry
    mid = len(arry)//2 
    left = arry[:mid]
    right = arry[mid:]

    left = magreSort(left)
    right = magreSort(right)

    return merge_towo_sorted_arry(left , right )




def partition(arry, start , end ):
    key_index = start
    key = arry[key_index]
    while  start < end :
        while start < len(arry) and  arry[start] <= key :
            start +=1

        while arry[end] > key : 
            end -=1

        if start < end :
            arr[start],arry[end]=arry[end],arry[start]


    arry[end],arry[key_index] = arry[key_index],arry[end] 

    return end 



def quickSort(arry, start, end ):
    if start< end :
        key_index = partition(arry, start , end)
        quickSort(arry, start, key_index -1) #letf
        quickSort(arry, key_index + 1, end ) #right


def max_digits(arry):
    m  = 0 
    for i in arry :
       m = max(m , i)
    return len (str(m)) 



from functools import reduce
def _map(arry):
    return reduce (lambda x,y: x+y , arry)

def RidexSort(arry, num_digits): 
    for digit in range(0, num_digits):
        packets = [[] for i in range(10)]
        for item in arry :
            num = item // 10 ** (digit) %10
            packets[num].append(item)
        arry = _map(packets)

    return arry



def CountingSort(array):
    size = len(array)
    output = [0] * size
    count = [0] * 10


    for i in range(0, size):
        count[array[i]] += 1


    for i in range(1, 10):
        count[i] += count[i - 1]


    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1


    for i in range(0, size):
        array[i] = output[i]


data = [4, 2, 2, 8, 3, 3, 1]
CountingSort(data)
print("Sorted Array by CountingSort : ")
print(data)



arry = [11, 5, 7 ,58 ,15 , 29]
quickSort(arry , 0 , len(arry)-1)
print("Sorted Array by quickSort : ")
print(arry)


arry1 = [11, 5, 5 ,58 ,15 , 29, 9 ,40]
print("Sorted Array by magreSort : ")
print(magreSort(arry1))

arry2 = [11, 5, 5 ,58 ,15 , 29, 9 ,40]
print("Sorted Array by RidexSort : ")
num = max_digits(arry2)
arry2  = RidexSort(arry2, num)
print (arry2)