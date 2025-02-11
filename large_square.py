def solution(A):
    max_square = 0
    count = 0

    for i in range(len(A)):
        if i == 0 or A[i] == A[i - 1]:
            count += 1
        else:
            count = 1
        
        current_square_size = min(A[i], count)
        max_square = max(max_square, current_square_size)
    return max_square

# Test cases
A1 = [1, 2, 2, 2, 4, 4, 5]
print(solution(A1))

A2 = [1, 2, 2, 4, 5]
print(solution(A2))

A3 = [10, 10, 10, 10]
print(solution(A3))