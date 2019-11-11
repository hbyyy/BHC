# 191111버전

# 리스트 입력받기
array_str = input('콤마로 구분하여 순서대로 숫자 입력> ').split(',')
array = list(map(int, array_str))
print(array, type(array))
print()

# 2차원 리스트 입력받기
n = int(input('1이상 50이하 입력> '))
commands = []
print('i,j,k 순서대로 콤마로 구분하여 숫자를 입력해주세요.')
for i in range(n):
    line_str = input('{} 세트 입력> '.format(i+1)).split(',')
    line_int = list(map(int, line_str))
    commands.append(line_int)
print(commands)
print()

# 함수 정의하기
def solution(array, commands):
    answer = []
    for n in range(len(commands)):
        i, j, k = commands[n][0], commands[n][1], commands[n][2]
        array_slice = array[i-1: j]
        array_slice.sort()
        answer.append(array_slice[k-1])
    return answer

print(solution(array, commands))
