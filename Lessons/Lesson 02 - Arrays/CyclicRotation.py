def solution(A, K):
    # write your code in Python 3.6
    # A와 동일한 길이의 V 초기화
    V = [0 for i in range(len(A))]

    # 원형 큐 구현 방법이랑 동일
    for i in range(len(A)):
        V[(i + K) % len(A)] = A[i]

    return V

