
def longestConsecutive(nums: list) -> int:
    """Return the length of the longest consective sequence of number in the given list.

    Parameter:
        nums(list): The list in which we want to find the longest seqeunce.
    
    Return:
        int: The len of the longest consective sequence.
    """

    consective_sequences = []
    sorted_nums = sorted(nums)
    current_sequence = 1

    if not nums:
        return 0
    
    for num in range(len(sorted_nums) - 1):

        if sorted_nums[num] == sorted_nums[num + 1]:
            continue

        if sorted_nums[num] + 1 == sorted_nums[num + 1]:
            current_sequence += 1

        else:
            consective_sequences.append(current_sequence)
            current_sequence = 1

    consective_sequences.append(current_sequence)

    return max(consective_sequences)