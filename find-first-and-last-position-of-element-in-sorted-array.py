def searchRange(nums, target):
        first = -1
        last = -1
        for i in range(len(nums)):
            if nums[i] == target:
                if first == -1:
                    first = i
                last = i
        return first, last

# test 1
nums1 = [5,7,7,8,8,10]
target1 = 8
print(searchRange(nums1, target1))

# test 2
nums2 = [5,7,7,8,8,10]
target2 = 6
print(searchRange(nums2, target2))

#test 3
nums3 = [2,2]
target3 = 2
print(searchRange(nums3,target3))