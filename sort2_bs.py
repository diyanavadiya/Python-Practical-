def sort(nums):
    n=len(nums);

    for i in range(0,n):
        for j in range(0,n-i-1):
            if(nums[j]>nums[j+1]):
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp
                
user_input = input("Enter numbers separated by commas: ")
nums= [int(x.strip()) for x in user_input.split(',') if x.strip()]

print("Original list:", nums)
sort(nums)
print("Sorted list:  ", nums)
