import random
 
# extra
nums1 = random.sample(range(100), 13)
nums2 = random.sample(range(100), 29)
print(nums1)
print(nums2)

print([num for num in nums1 if num in nums2])