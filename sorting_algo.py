A = [5,15,4,58,12,8]


#Selection Sort
# in this selection sort algorithm, time complexity is O(n^2) as it have to go through list for n times and again n times within. 
def selection_sort(list):
    for i in range(len(list)):
        min_ind = i
        for j in range (i+1 , len(list)):
            if list[min_ind] > list[j] :
                min_ind = j
        list[min_ind] , list[i] = list[i] , list[min_ind]
    return list

# print(selection_sort(A))




#Bubble Sort
def bubble_sort(list):
    for i in range(len(list)):
        print('switching')
        for j in range(len(list) - i -1):
            if(list[j] > list[j+1]):
                list[j], list[j+1] = list[j+1] , list[j]
            print(list)
    return list

# print(bubble_sort(A))



#Insertion Sort
# the first loop have to go through the loop n times and in the worst case the inner loop have to go through (n-1) times.
# so the time complexity is n(n-1)=> O(n^2)

def insertion_sort(list):
    for i in range(len(list)):
        key = list[i]
        j = i-1

        while j>=0 and list[j+1]<list[j]:
            list[j+1] = list[j]
            j = j-1

        list[j+1] = key
    return list

# print(insertion_sort(A))


#MergeSort

def merge_sort(list):
    if(len(list) > 1):
        mid = len(list)//2
        left = list[: mid]
        right = list[mid :]
        print(left)
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        print(left[0])

        while (i < len(left) and j < len(right)):
            # print(len(left))
            # print(i)
            if(i< len(left)):
                list[k] = left[i]
                i+=1

            else:
                list[k] = right[j]
                j+=1

            k +=1
            # print(list)


        while i < len(left):
            list[k] = left[i]
            i+=1
            k+=1
            # print(list)


        while j < len(right):
            list[k] = right[j]
            j+=1
            k+=1
            # print(list)
        # print(k)
        
    # return list
    # list[k]

merge_sort(A)
# print(A)