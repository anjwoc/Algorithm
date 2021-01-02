def solution(phone_book):
    answer = True
    dic = {i: 1 for i in phone_book}

    for phone_number in phone_book:
        tmp = ""
        for number in phone_number:
            tmp += number
            if tmp in dic and tmp != phone_number:
                answer = False
                return answer
    return answer
