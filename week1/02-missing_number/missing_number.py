def find_missing(nums):
    for i in range(len(nums)-1):
        if nums[i+1] - nums[i] != 1:
            return nums[i] + 1
    return 0

print(find_missing([1, 2, 3, 5, 6]))



# 0, 1, 2, 3, 4 >> i
# 1, 2, 3, 5, 6 >> nums
# 1 >> num
# 2 >> next
# 3 >> next
# 5 >> next
# 6 >> next