# largesquare-codility
# Largest Square in Non-Decreasing Columns

## Problem Statement
Given an array `A` of `N` non-decreasing integers, where each integer represents the height of a column made of 1x1 blocks, the goal is to find the side length of the largest square that can be formed using consecutive columns.

### Example Inputs & Outputs

#### Example 1
**Input:**
```python
A = [1, 2, 2, 2, 4, 4, 5]
```
**Output:**
```python
3
```

#### Example 2
**Input:**
```python
A = [1, 2, 2, 4, 5]
```
**Output:**
```python
2
```

#### Example 3
**Input:**
```python
A = [10, 10, 10, 10]
```
**Output:**
```python
4
```

## Solution Approach
### Observations
- The square’s side length is constrained by both:
  - The **height** of the shortest column in a valid subarray.
  - The **number of consecutive columns** forming the square.
- We traverse the array while maintaining a `count` of consecutive columns that can form a square.
- If the height increases, the count resets.

### Algorithm
1. Initialize `max_square = 0` and `count = 0`.
2. Traverse the array:
   - If `A[i] == A[i-1]`, continue counting consecutive columns.
   - If `A[i] > A[i-1]`, reset `count` to `1`.
   - Compute the possible square size: `min(A[i], count)`.
   - Update `max_square` if needed.
3. Return `max_square` at the end.

### Implementation
```python
def solution(A):
    max_square = 0
    count = 0

    for i in range(len(A)):
        if i == 0 or A[i] == A[i - 1]:  # Continue counting for the same height
            count += 1
        else:
            count = 1  # Reset count when height increases

        current_square_size = min(A[i], count)
        max_square = max(max_square, current_square_size)

    return max_square

# Test cases
A1 = [1, 2, 2, 2, 4, 4, 5]
print(solution(A1))  # Expected output: 3

A2 = [1, 2, 2, 4, 5]
print(solution(A2))  # Expected output: 2

A3 = [10, 10, 10, 10]
print(solution(A3))  # Expected output: 4
```

## Complexity Analysis
- **Time Complexity:** `O(N)`, since we traverse the array once.
- **Space Complexity:** `O(1)`, as we use only a few extra variables.

## Edge Cases Considered
- **Single Column (`N=1`)**: `[3]` → Output: `1`
- **All Equal Heights**: `[5, 5, 5, 5, 5]` → Output: `5`
- **Strictly Increasing Heights**: `[1, 2, 3, 4]` → Output: `2`

## Conclusion
This solution efficiently finds the largest possible square in a sequence of non-decreasing columns using a single-pass approach while maintaining an optimal count tracking mechanism.

