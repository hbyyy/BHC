def solution(seoul):
    '''
    seoul 리스트에는 'Kim'이 무조건 하나 존재한다. Kim의 인덱스를 찾아 '김서방은 _에 있다' 의 포멧으로 답을 리턴한다.
    '''
    # 'Kim'의 인덱스를 enumerate()를 이용해 검색
    for i, s in enumerate(seoul):
        if s == 'Kim':
            index_kim = i
            break
    answer = f'김서방은 {index_kim}에 있다'
    return answer
