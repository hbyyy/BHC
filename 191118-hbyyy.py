# def solution(phone_book):
#     min_number_len = len(phone_book[0])
#     for i in range(1, len(phone_book)):
#         if min_number_len > len(phone_book[i]):
#             min_number_len = len(phone_book[i])
#     for i in range(0, len(phone_book)):
#         if min_number_len < len(phone_book[i]):
#             phone_book[i] = phone_book[i][0:min_number_len]
#         print(phone_book)
#     if len(phone_book) == len(set(phone_book)):
#         return True
#     else:
#         return False

def solution(phone_book):
    for i in range(len(phone_book) -1):
        for j in range(i +1, len(phone_book)):
            # if len(phone_book[i]) > len(phone_book[j]):
            #     continue
            if phone_book[i] == phone_book[j][0:len(phone_book[i])]:
                return False
            elif phone_book[i][0:len(phone_book[j])] == phone_book[j]:
                return False
            else:
                pass
    else:
        return True
         
