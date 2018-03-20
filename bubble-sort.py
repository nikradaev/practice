#Buble sort array algorithm function

x = [20, 5, 6, 7, 9, 10, 100, 30, 4, 0, 999, -5]

def sort (a):
    l = len(a)
    for j in range(l):
        for i in range(l - j):
            #find the min & swap in the original array
            #but finding the min index only within cutoff portion [i:l-j]
            min2_index = minn(a[i : l - j])
            #swapping with i and min_index+i - because we moved on i and min will be + i
            a = swap(i, min2_index + i, a)
            #find the max & swap in the original
            #but finding the max index only within cutoff portion [i:l-j]
            max2_index = maxx(a[i : l - j])
            #swapping with  and min_index+i - because we moved on i and max will be l - j - 1
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
