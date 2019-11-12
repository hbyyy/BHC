def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        command = commands[i]
        tempArr = sorted((array[command[0]-1:command[1]]))
        answer.append(tempArr[command[2]-1])
    return answer


