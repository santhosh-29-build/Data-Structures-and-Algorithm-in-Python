nums=[1,2,3,4,5,6]

nums.append(6)
nums.extend([8,9])
nums.insert(6,7)
nums.remove(9)
a=nums.pop(4)
print(nums.index(6))
print(nums.count(6))
nums.sort()
nums.reverse()
print(a)
print(nums)