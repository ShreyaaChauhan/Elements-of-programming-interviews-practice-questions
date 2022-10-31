def concatenation_of_array(nums):
    n = len(nums)
    for i in range(n):
        nums.append(nums[i])
    print(nums)


nums = [1, 2, 3, 4]
concatenation_of_array(nums)
