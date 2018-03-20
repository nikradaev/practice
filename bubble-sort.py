#Buble sort array algorithm function

x = [20, 5, 6, 7, 9, 10, 100, 30, 4, 0, 999, -5]

def sort (a):
    l = len(a)
    for j in range(l):
        #slicing to the center
        for i in range(l - j):
            #find the min & swap in the original array
            #but finding the min index only within cutoff portion [i:l-j]
            min_index = minn(a[i : l - j])
            #swapping with i and min_index+i - because desired location for min is i and current min is minindex + i
            a = swap(i, min_index + i, a)
            #find the max & swap in the original array
            #but finding the max index only within cutoff portion [i:l-j]
            max_index = maxx(a[i : l - j])
            #swapping with l - j - 1 and max_index+i - because desired location for max is l - j - 1 and current max is maxindex + i
            a = swap(l - j - 1, max_index + i, a)
    return a
    
def minn(a):
    min_value = a[0]
    min_index = 0
    for x in range(len(a)):
        if a[x] < min_value:
            min_value = a[x]
            min_index = x
    return min_index

def maxx(a):
    max_value = a[0]
    max_index = 0
    for x in range(len(a)):
        if a[x] > max_value:
            max_value = a[x]
            max_index = x
    return max_index

def swap(index1, index2, arr):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp
    return arr
    
x = sort(x)
print(x)
