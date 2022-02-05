# 217 contains duplicate
# time: O(nlogn) sorted array

#hashset  mem: O(n)
def containsDup(nums) -> bool:
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False