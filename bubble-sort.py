#Buble sort array algorithm function

x = [8, 9, 7, 10, 6, 4, 0, 100, -5, 30, 7, 10, 999, 200, 15]

def bubbleSort(a):
    def swap(x, y):
        temp = a[x]
        a[x] = a[y]
        a[y] = temp
    #outer loop
    for j in range(len(a)): 
        #slicing to the center, inner loop, python style
        for i in range(j, len(a) - j):  
            #find the min index and swap
            if a[i] < a[j]:
                swap(j, i)
            #find the max index and swap
            if a[i] > a[len(a) - j - 1]:
                swap(len(a) - j - 1, i)
    return a

x = bubbleSort(x)
print(x)
