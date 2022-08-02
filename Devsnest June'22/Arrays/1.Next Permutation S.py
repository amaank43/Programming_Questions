# Link:https://devsnest.in/algo-challenges/next-permutation?tab=question
    
def solve(n, nums):
    # CODE HERE
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1        
    if i < 0:
        nums.sort()
        return    
    j = len(nums) - 1
    while j >= 0 and nums[i] >= nums[j]:
        j -= 1        
    nums[i], nums[j] = nums[j], nums[i]
    nums[i+1:] = nums[i+1:][::-1]
    return nums  
