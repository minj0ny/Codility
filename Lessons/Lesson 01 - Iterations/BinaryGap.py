def solution(N):
    # write your code in Python 3.6
    b = format(N, 'b')

    zero_list = list()
    b_gaps = 0

    for i in b:
        if i == '1':
            if len(zero_list) > 0:
                if len(zero_list) > b_gaps:
                    b_gaps = len(zero_list)
                zero_list.clear()
        else:
            zero_list.append(0)

    return b_gaps
