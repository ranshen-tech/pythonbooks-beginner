# def pivotIndex(nums):
#     a = 0
#     for i in range(len(nums)):
#         b = sum(nums) - a - nums[i]
#         if a == b:
#             return i
#         a += nums[i]
#     return -1

# nums = [1,2,3,4,5]
# print(pivotIndex(nums))


def pivotIndex(nums):
    a = 0
    for i in range(len(nums)):
        if a * 2 + nums[i]== sum(nums):
            return i
        a += nums[i]
    return -1

nums = [1,2,3,3]
print(pivotIndex(nums))