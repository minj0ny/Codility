# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6

    #파이썬에서 sorted() 메소드는 O(N*log(N)) 의 성능을 가진다고 한다
    A = sorted(A)

    for i in range(0, len(A), 2):
        if i == len(A) - 1:
            return A[i]
        if A[i] != A[i + 1]:
            return A[i]

