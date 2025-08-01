def sort(nums):
    n = len(nums)
    for i in range(n):
        key = i
        
        for j in range(i + 1, n):
            if nums[j] < nums[key]:
                key = j
        
        nums[i], nums[key] = nums[key], nums[i]



nums = [10,8,1,2,7]
sort(nums)
print(nums)
