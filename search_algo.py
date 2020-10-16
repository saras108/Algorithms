def linear_search(list , num):
    #the time complexity of this algo is O(n) as in the worst case it have to go through all the list.

    for i in range(len(list)):
        if(list[i] == num ):
            return i
    return "The data which you have searched is not found in the Array."
    



def binary_search(list , num , starting , ending):
    #the time complexity of this algo is O(log base 2 n) as
    #1st iteration: n/2 part on list is seprated
    #2nd iteration: n/4 part is seprated
    #3rd iteration: n/8 part of list is seperated
    # and in the worst case : n/n part of to list is seprated, so its time complexity is O(log base 2 n)


    if(starting > ending):
        #if ending index is greater then the starting index, the alogo have been through all the list and it havent found on the list. 
        return "The data which you have entered does not lies on the list."

    mid = (ending+starting)//2

    print(list[starting : ending])

    if list[mid] == num:
        return mid
    elif list[mid] > num:
        return binary_search(list ,num ,starting , mid-1)
    else:
        return binary_search(list, num , mid+1 , ending )


def get_array():
    my_arr = []

    arr_num = int(input("Enter the number of elements"))

    for i in range(arr_num):
        a = int(input("enter the number"))
        my_arr.append(a)
    
    return my_arr
        

list = get_array()


# get_index = linear_search(list , int(input("the number to be found")))
# print(get_index)

get_index = binary_search(list , int(input("Number you want to search")) , 0 , len(list))
print(get_index)



# A = [2,6, 9,10 , 11 ,12, 15 ,18 ]
# num = 12
# a = binary_search(A , num , 0 ,len(A))

# print(a)