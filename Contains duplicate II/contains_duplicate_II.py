
def contains_duplicate(nums, k):

    hash_set = set()

    for num in range(len(nums)):
        if nums[num] in hash_set:
            return True

        hash_set.add(nums[num])

        if len(hash_set) > k:
            hash_set.remove(nums[num - k])

    return False
        