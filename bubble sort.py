nums=[4,3,5,1,2]
def sort(nums):
    n=len(nums);

    for i in range(0,n):
        for j in range(0,n-i-1):
            if(nums[j]>nums[j+1]):
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp
                
sort(nums)
print(nums)
