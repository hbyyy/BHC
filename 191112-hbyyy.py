
# solution 1

def solution(n):
    str_wm = '수박'
    counter = False
    answer = ''
    for i in range(n):
        answer += str_wm[counter]
        counter = not counter
    return answer

# solution 2


def solution(n):
    str_wm = '수박'
    answer = ''
    if n % 2 == 0:
        answer = str_wm * (n//2)
    else:
        answer = str_wm * (n//2) + str_wm[0]
    return answer
