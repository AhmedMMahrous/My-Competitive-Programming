def Two_Sum (nums,target):
        
    numMap = {}
    n = len(nums)

    for i in range(n):
        complement = target - nums[i]
        if complement in numMap:
            return [numMap[complement], i]
        numMap[nums[i]] = i

    return []  # No solution found
print(Two_Sum([1,2,3],5))


def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        secondItem = target - nums[i]
        for j in range (i+1,n):
            if secondItem == nums[j]:
                return [i,j]

nums = [2,7,11,15]
target = 22
print(twoSum(nums, target))