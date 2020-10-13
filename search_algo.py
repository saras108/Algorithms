def linear_search(list , num):
    for i in range(len(list)):
        if(list[i] == num ):
            return i
    return "the data which you have searched is not found."


def binary_search(list , num):
    #first sorting the list

    #then use the binary search


    pass



def get_array():
    my_arr = []

    arr_num = int(input("Enter the number of elements"))

    for i in range(arr_num):
        a = int(input("enter the number"))
        my_arr.append(a)
    
    return my_arr
        

list = get_array()


get_index = linear_search(list , int(input("the number to be found")))
print(get_index)


# A = [2,6, 9,10 , 11 ,12, 15 ,18]
# num = 18