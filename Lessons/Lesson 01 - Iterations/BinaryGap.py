def solution(N):
    # write your code in Python 3.6
    # 입력값을 2진수로 변환
    b = format(N, 'b')

    # 0을 저장할 리스트와 0의 최대 시퀀스값 초기화
    zero_list = list()
    b_gaps = 0

    for i in b:
        # 1일 때(0카운트를 시작하는 1과 끝내는 1로 나누어서 해석)
        if i == '1':
            # 0 저장 리스트의 값이 0보다 크다는 의미는 끝내는 1일 때 라고 생각함
            if len(zero_list) > 0:
                # 0의 최대 시퀀스 값 비교 후 저장
                if len(zero_list) > b_gaps:
                    b_gaps = len(zero_list)
                # 다음 0 저장을 위하여 리스트 초기화
                zero_list.clear()
        else:
            zero_list.append(0)

    return b_gaps
