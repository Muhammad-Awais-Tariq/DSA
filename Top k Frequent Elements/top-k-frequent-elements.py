
# ------------------------------- My solution ------------------------------

def topKFrequent(nums: list, k: int) -> list:
    """Return the k elments that has highest frequency of elements in the nums.

    Parameters:
        nums (list): The list of the numbers.
        k (int) : The total number of elements that we hv to return.
    
    Return:
        list : The final list of elements.
    """

    hash_map = {}

    for num in nums:
        if num in hash_map:
            hash_map[num] += 1
        else:
            hash_map[num] = 1

    temp_answer = [(None , float('-inf'))] * k

    for key , value in hash_map.items():
        if value > temp_answer[0][1]:
            temp_answer[0] = (key , value)
            temp_answer = sorted(temp_answer , key= lambda x : x[1])

    return [value[0] for value in temp_answer]