# This folder contain the possible examples related to sliding window problems

## 1. Find maximum (or minimum) sum of a subarray of size k

Description:

Input : arr[] = {100, 200, 300, 400}, k = 2

Output : 700

Input : arr[] = {1, 4, 2, 10, 23, 3, 1, 0, 20}, k = 4

Output : 39

Explanaton: We get maximum sum by adding subarray {4, 2, 10, 23} of size 4.

```
# O(n) solution

# returns maximum sum in a subarray of size k.
def maxSum_logic(nums, k):

    n = len(nums)

    # k must be smaller than n
    if n < k:
        print('Invalid')
        return -1

    # Calculate first sum of window of size k
    sum = 0

    for i in range(k):
        sum += nums[i]


    # Calculate the remaining window by removing first element of previous
    # window and adding last element of current window.

    currSum = sum

    for i in range(k,n):
        currSum += nums[i] - nums[i - k]
        sum = max(sum, currSum)

    return sum


arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4

max_sum = maxSum_logic(arr,k)
print(max_sum)

# Output is 39

```
