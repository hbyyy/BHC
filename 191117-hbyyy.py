def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        command = commands[i]
        
        # tempArr = sorted((array[command[0]-1:command[1]]))
        # 선택 정렬 구현
        tempArr = array[command[0]-1:command[1]]
        for i in range(len(tempArr) -1):
            min_value = tempArr[i]
            for j in range(i, len(tempArr)):
                if min_value >= tempArr[j]:
                    min_value = tempArr[j]
                    min_idx = j
            tempArr[i], tempArr[min_idx] = tempArr[min_idx], tempArr[i]
                
                
        answer.append(tempArr[command[2]-1])
    return answer
