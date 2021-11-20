nums = [3,2,1,5,6,4]
k=2

def kbig(nums, k):
    nums.sort(reverse = True)
    print(nums[k-1])

kbig(nums,k)
