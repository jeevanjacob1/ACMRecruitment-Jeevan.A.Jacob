# Array Rotation Problem and Solution

## Problem Statement

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is a non-negative integer.

For example, rotating `[1, 2, 3, 4, 5, 6, 7]` by `3` steps results in `[5, 6, 7, 1, 2, 3, 4]`.

## Solution Approach

1. Normalize `k` by taking `k = k % len(nums)` to handle cases when `k` is larger than the length of the array.
2. Reverse the entire array.
3. Reverse the first `k` elements.
4. Reverse the remaining `len(nums) - k` elements.

This method performs the rotation **in-place** with O(n) time complexity and O(1) space complexity.

---

## Example

Original array: `[1, 2, 3, 4, 5, 6, 7]`  
k = 3

Step 1: Reverse entire array: `[7, 6, 5, 4, 3, 2, 1]`  
Step 2: Reverse first k elements: `[5, 6, 7, 4, 3, 2, 1]`  
Step 3: Reverse remaining elements: `[5, 6, 7, 1, 2, 3, 4]`

Final rotated array: `[5, 6, 7, 1, 2, 3, 4]`
