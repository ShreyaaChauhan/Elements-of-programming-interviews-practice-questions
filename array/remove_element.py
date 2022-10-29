def remove_element(nums, value):
    i = 0
    for j in range(len(nums)):
        if nums[j] != value:
            nums[i] = nums[j]
            i = i + 1
    print(i)


nums = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 4, 4, 4, 5]
value = 2
remove_element(nums, value)
