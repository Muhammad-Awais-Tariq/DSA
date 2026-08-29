
# ---------------- Optimal Solution ---------------
def firstMissingPositive(nums: list) -> int:
    """Returns the first positive missing number in the list.

    Paramters:
        nums (list): The list of nums we want to check.
    
    Return:
        int: The first positive missing number in the list.
    """

    n = len(nums)
    contains = 0

    for i in range(n):
        if nums[i] == 1:
            contains += 1
            break

    if contains == 0:
        return 1
    
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = 1

    for i in range(n):
        a = abs(nums[i])
        if a == n:
            nums[0] = -abs(nums[0])
        else:
            nums[a] = -abs(nums[a])

    for i in range(1, n):
        if nums[i] > 0:
            return i
        
    if nums[0] > 0:
        return n
    
    return n + 1




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

