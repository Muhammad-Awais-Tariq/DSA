
# ------------------------ My solution --------------------------------
def productExceptSelf(nums: list) -> list:
    """Return the product of all elements except the element at each index.

    Parameters:
        nums (list): The list of numbers.

    Returns:
        list: A list containing the product of all elements except
            the element at the corresponding index.
    """

    total_size = len(nums)
    final_array = [None] * total_size

    for i in range(total_size):
        product = 1
        for j in range(total_size):
            if i == j:
                continue
            product *= nums[j]
        final_array[i] = product

    return final_array

print(productExceptSelf([-1,1,0,-3,3]))