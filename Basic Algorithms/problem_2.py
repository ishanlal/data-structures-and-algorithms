def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    key = number
    start = 0
    end = len(input_list)-1
    return fast_search(input_list, start, end, key)

def fast_search(arr, start, end, key):
    if start > end:
        return -1

    mid = (start + end) // 2

    if arr[mid] == key:
        return mid

    # if array is already sorted, just search for key
    if arr[start] <= arr[mid]:
        if key >= arr[start] and key <= arr[mid]:
            return fast_search(arr, start, mid - 1, key)
        return fast_search(arr, mid + 1, end, key)

    # pivot encountered, search the other half of the array
    if key >= arr[mid] and key <= arr[end]:
        return fast_search(arr, mid + 1, end, key)
    return fast_search(arr, start, mid - 1, key)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print(linear_search(input_list, number))
        print(rotated_array_search(input_list, number))
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
#edge test 1  empty string
test_function([[], 1])
#edge test 2  large list
test_list=[i for i in range (1011,10000)]+[i for i in range (0,1011)]
#print (test_list)
test_function([test_list, 6])
#egde test 3  large list with negative numbers
test_list=[i for i in range (1011,10000)]+[i for i in range (-1000,1011)]
#print (test_list)
test_function([test_list, -60])
