def remove_duplicates(nums):
    i, j = 0, 1
    while j <= len(nums) - 1:
        if nums[i] != nums[j]:
            i = i + 1
            nums[i] = nums[j]
        j = j + 1
    del nums[i + 1 :]
    # nums = nums[: i + 1]
    print(nums)


nums = [1, 2, 3, 3, 3, 4, 4, 4]
remove_duplicates(nums)
