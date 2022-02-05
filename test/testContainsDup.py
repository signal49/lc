def testContainsDup(nums)-> bool:
    hashset = set()

    for i in nums:
        if i in hashset:
            return True
        else:
            hashset.add(i)
    return False

arr = [1,23,34,5,6,6]
print(testContainsDup(arr))


