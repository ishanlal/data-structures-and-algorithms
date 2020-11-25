def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min_ = ints[0]
    max_ = ints[0]
    for i in range(len(ints)):
        if ints[i] > max_:
            max_ = ints[i]
        elif ints[i] < min_:
            min_ = ints[i]
    return (min_, max_)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
#egde case 1: large list
edge_1 = [i for i in range(200,2000)]
random.shuffle(edge_1)
print ("Pass" if ((200, 1999) == get_min_max(edge_1)) else "Fail")
#egde case 2: large list   with negative numbers
edge_2 = [i for i in range(-20000000,-2000)]
random.shuffle(edge_2)
print ("Pass" if ((-20000000, -2001) == get_min_max(edge_2)) else "Fail")
