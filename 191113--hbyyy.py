def solution(a, b):
    week = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    num_of_day_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_of_year = 0
    
    # a월 b일까지 총 지난 일자를 계산
    for i in range(0, a -1):
        day_of_year += num_of_day_in_month[i] 
    day_of_year += b
    answer = week[(day_of_year % 7) -1 ]
    return answer




    
