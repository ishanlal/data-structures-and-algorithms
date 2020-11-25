def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    negative = False
    if number == -1:
        return 'i'
    if number < 0:
        negative = True
        number = number * (-1)
    if number == 0 or number == 1:
        return number
    start = 1
    end = number
    while (start <= end):
        mid = (start + end) // 2
        if (mid*mid == number):
            ret_index = mid
            break
        if (mid*mid < number):
            start = mid + 1
            ret_index = mid
        else:
            end = mid - 1
    if negative is True:
        ret_index = str(ret_index)
        ret_index = ret_index + 'i'
        return ret_index
    else:
        return ret_index

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  ('3i' == sqrt(-9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (6 == sqrt(40)) else "Fail")
print ("Pass" if  ('6i' == sqrt(-40)) else "Fail")
print ("Pass" if  (31622 == sqrt(10**9)) else "Fail")
