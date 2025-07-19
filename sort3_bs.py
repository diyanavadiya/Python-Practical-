def sort(nums):
    n=len(nums);

    for i in range(0,n):
        for j in range(0,n-i-1):
            if(nums[j]>nums[j+1]):
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp
def main():
    size = int(input("Enter the number of elements: "))
    nums = []
    for i in range(size):
        num = int(input(f"Enter element {i + 1}: "))
        nums.append(num)

    print("\nOriginal array:", nums)
    sort(nums)
    print("Sorted array:  ", nums)

if __name__ == "__main__":
    main()
