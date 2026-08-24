
# ------------------------ optimal solution --------------------------------
# def productExceptSelf(nums):

#     answers = [1] * len(nums)

#     pre = 1
#     post = 1

#     for i in range(len(nums)):
#         answers[i] = pre
#         pre = pre * nums[i]

#     for i in range(len(nums)-1 , -1 ,-1):
#         answers[i] *= post
#         post = post * nums[i]

#     return answers

# ------------------------ Semi optimal solution --------------------------------
# def productExceptSelf(nums: list) -> list:

#     prefix = [1] * len(nums)
#     postfix = [1] * len(nums)

#     for i in range(1 , len(nums)):
#         prefix[i] = prefix[i-1] * nums[i-1]

#     for i in range(len(nums)-2 , -1 , -1):
#         postfix[i] = postfix[i+1] * nums[i+1]

#     answer = [prefix[i] * postfix[i] for i in range(len(nums))]

#     return answer

# ------------------------ My solution --------------------------------
# def productExceptSelf(nums: list) -> list:
#     """Return the product of all elements except the element at each index.

#     Parameters:
#         nums (list): The list of numbers.

#     Returns:
#         list: A list containing the product of all elements except
#             the element at the corresponding index.
#     """

#     total_size = len(nums)
#     final_array = [None] * total_size

#     for i in range(total_size):
#         product = 1
#         for j in range(total_size):
#             if i == j:
#                 continue
#             product *= nums[j]
#         final_array[i] = product

#     return final_array

# print(productExceptSelf([-1,1,0,-3,3]))