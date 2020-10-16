import math


#ask the input array from user
def get_array():
    my_arr = []

    arr_num = int(input("Enter the number of elements"))

    for i in range(arr_num):
        a = int(input("enter the number"))
        my_arr.append(a)

    return my_arr

list = get_array()


#Binary Search
    # the time complexity of this algo is O(log base 2 n) as
    # 1st iteration: n/2 part on list is seprated
    # 2nd iteration: n/4 part is seprated
    # 3rd iteration: n/8 part of list is seperated
    # and in the worst case : n/n part of to list is seprated, so its time complexity is O(log base 2 n)


def binary_search_recursion(list, num, starting, ending):

    if(starting > ending):
        # if starting index is greater then the ending index, the alogo have been through all the list and it havent found on the list.
        return "The data which you have entered does not lies on the list."

    mid = (ending+starting)//2

    # print(list[starting: ending])

    if list[mid] == num:
        return mid

    elif list[mid] > num:
        return binary_search_recursion(list, num, starting, mid-1)

    else:
        return binary_search_recursion(list, num, mid+1, ending)


def binary_search_iteration(list , num):

    mid = 0
    starting = 0
    ending = len(list)-1

    while(starting <= ending):
        mid = (starting+ending)//2

        if list[mid]== num:
            return mid
        
        elif list[mid] < num:
            starting = mid+1

        else:
            ending = mid-1

    return "The data which you are searching is not available in this list."



# get_index = binary_search_recursion(list, int(input("Number you want to search")), 0, len(list)-1)
# print(get_index)

# get_index = binary_search_iteration(list, int(input("Number you want to search")))
# print(get_index)




# linear Search
    # the time complexity of this algo is O(n) as in the worst case it have to go through all the list.

def linear_search_iteration(list, num):

    for i in range(len(list)):
        if(list[i] == num):
            return i

    return "The data which you have searched is not found in the Array."


def linear_search_recursion(list, num , starting , ending):

    # print(list , num , starting , ending)
    # print(list[starting: ending])

    if starting >ending:
        return "The data which you have searched is not found in the Array."
    
    if list[starting] == num:
        return starting
    
    else:
        return linear_search_recursion(list , num , starting+1 , ending)


# get_index = linear_search_iteration(list , int(input("the number to be found")))
# print(get_index)

# get_index = linear_search_recursion(list , int(input("the number to be found")) , 0, len(list)-1)
# print(get_index)





#jump search
    #consider we have n elements,  to find the element in the list using jump search , we have to make a block "m" and the index jumps from block to block.
    #the starting index and ending index of block are checked and if the number lies between them we have to go throgh the linear search on that block
    #so the time complexity is (n/m) for the block nodes and (m-1) for the linear search so its total time complexity is O((m/n)+(m-1)).
    #th optimum value of m is root n.  derivation of the time complexity with respect to m is root n
    #d((n/m)+(m-1))/dm =0
    #(-n/m^2 + 1) =0
    #n/m^2 = 1
    #n = m^2
    #m = root n

def jump_search_iteration(list , num):
    n =len(list)
    step = int(math.sqrt(n))
    prev = 0
    id = step

    while list[id] <= num:
            
        if(list[id] == num):
            return id

        elif list[id] < num:
            # print(list[id])
            prev = id
            id = prev+id
                    
            if(id > n-1):
                id = n-1
                if list[id] < num:
                    return "The number doesnt include in the list"
    

    return linear_search_recursion(list , num , prev , id)



# get_index = jump_search_iteration(list , int(input("the number to be found")))
# print(get_index)


def jump_search_recursion(list , num , step , prev , id):
    if list[id] <= num:
        if list[id]== num:
            return id
        else:
            prev = id
            id = id + step

            if(id > len(list)-1):
                id = len(list)-1

                if list[id] < num:
                    return "The number doesnt include in the list"

        return jump_search_recursion(list , num , step , prev , id)
    
    else:
        return linear_search_recursion(list , num , prev , id)


# get_index = jump_search_recursion(list , int(input("the number to be found")) ,  int(math.sqrt(len(list))), 0 , int(math.sqrt(len(list))))
# print(get_index)




A = [2,6, 9,10 , 11 ,12, 15 ,18, 20, 21 , 22 ,25 ]
num = 1
# b = jump_search_iteration(A , num)
# a = jump_search_recursion(A, num, int(math.sqrt(len(A))), 0 , int(math.sqrt(len(A))))

# print(a)


# print(int(math.sqrt(5)))