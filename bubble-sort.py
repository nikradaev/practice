#Buble sort array algorithm function

x = [20, 5, 6, 7, 9, 10, 100, 30, 4, 0, 999, -5]

def sort (a):
    
    l = len(a)
    
    for j in range(l):
    
        for i in range(l - j):

            #find the min

            min2_index = minn(a[i : l - j])
            a = swap(i, min2_index + i, a)
            

            #find the max

            max2_index = maxx(a[i : l - j])
            a = swap(l - j - 1, max2_index + i, a)
            
    return a
    

def minn(a):
    min1 = a[0]
    min_index = 0
    for x in range(len(a)):
        if a[x] < min1:
            min1 = a[x]
            min_index = x
    return min_index


def maxx(a):
    max1 = a[0]
    max_index = 0
    for x in range(len(a)):
        if a[x] > max1:
            max1 = a[x]
            max_index = x
    return max_index


def swap(i1, i2, arr):
    temp = arr[i1]
    arr[i1] = arr[i2]
    arr[i2] = temp
    
    return arr
    
    
    
x = sort(x)
print(x)
