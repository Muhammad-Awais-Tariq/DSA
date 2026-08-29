
# ----------------- My solution --------------------
def firstMissingPositive(nums: list) -> int:
    """Returns the first positive missing number in the list.

    Paramters:
        nums (list): The list of nums we want to check.
    
    Return:
        int: The first positive missing number in the list.
    """

    sorted_num = sorted(nums)
    expected = 1

    for num in sorted_num:
        if num == expected:
            expected += 1
        elif num > expected:
            break

    return expected

print(firstMissingPositive([7,8,9,11,12]))

