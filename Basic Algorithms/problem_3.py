def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    temp = input_list
    first = ""
    second = ""
    max_ = 0
    max_index = 0
    for k in range(len(temp)):
        max_ = max(temp)
        max_index = temp.index(max_)
        if (k % 2 == 0):
            first += str(max_)
        else:
            second += str(max_)
        temp.remove(max_)
    first = int(first)
    second = int(second)
    return [first, second]

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
#egde case 1: empty list
test_function([[0,0], [0, 0]])
#edge case 2: large set and large numbers
test_function([[i for i in range(0,10)], [int("".join(map(str,range(9,-1,-2)))), int("".join(map(str,range(8,-1,-2))))]])
#edge case 3: very large set and large numbers
test_function([[i for i in range(0,10000)], [int("".join(map(str,range(9999,-1,-2)))), int("".join(map(str,range(9998,-1,-2))))]])
