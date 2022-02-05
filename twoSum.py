# 1.  Two Sum
# HashMap: val, index
# time: O(n) and mem O(n)

def twoSum(nums, target):
    prevMap = {} # val: index
    
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
    return

arr = [1,4,3,6,7]
target = 7
print(twoSum(arr, target))


