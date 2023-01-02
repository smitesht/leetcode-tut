from typing import List

def twoSum(nums: List[int], target:int):
  hashmap = {}

  for ind, num in enumerate(nums):
    diff = target - num
    if diff in hashmap:
      return [hashmap[diff],ind]
    hashmap[num] = ind
   


# Test
twoSum([3,2,4],6)