# -*- coding: utf-8 -*-
import sys

sys.setdefaultencoding("utf-8")
ONE_DIGIT = map(
    unicode, ["", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]
)  # 한 자릿수 숫자를 읽은 것
UNIT_S = [u"십", u"백", u"천"]  # 네 자리 이하의, 작은 단위들
UNIT_B = map(unicode, ["", "만 ", "억 ", "조 ",],)  # 네 자리 이상의, 큰 단위들


def get_input():
    return [int(i) for i in raw_input()]


def num_kor_read(num):  # num은 각 자리 숫자들의 리스트

    digits = len(num)  # 숫자 자릿수
    if digits == 1:
        return ONE_DIGIT[num[0]]  # 한 자릿수 숫자의 경우 one_digit에서 해당하는 숫자를 돌려준다.
    if digits <= 4:  # 숫자 자릿수가 4자리 이하일 경우 가장 앞자리를 뽑아 먼저 읽고 나머지를 처리한다.
        head = num[0]  # 가장 앞자리 수
        if head == 0:  # 가장 앞자리가 0인 경우
            return num_kor_read(num[1:])
        part_read = []
        if head != 1:  # 가장 앞자리가 1이 아닌 경우
            part_read.append(ONE_DIGIT[head])
        part_read.append(UNIT_S[digits - 2])  # 단위 추
        part_read.append(num_kor_read(num[1:]))  # 뒷부분을 재귀를 이용해 읽는다.
        return "".join(part_read)
    else:  # 가독성을 위해 else 문을 사용한다.
        # 자릿수가 4의 배수가 아니면 앞자리에 0을 추가해 4의 배수로 만든다.
        if digits % 4 != 0:
            longer_num = [0 for i in xrange(4 - digits % 4)]
            digits += 4 - digits % 4
        else:
            longer_num = []
        longer_num.extend(num)
        part_read = []
        for i in xrange(digits / 4):  # 앞에서부터 네 자리씩 처리한다.
            temp = num_kor_read(longer_num[4 * i : 4 * i + 4])
            if temp == "":
                continue  # 0000의 예외처리
            part_read.append(temp)
            part_read.append(UNIT_B[digits / 4 - i - 1])  # 단위 추가
        return "".join(part_read)


def main():
    num = get_input()
    if num == [0]:
        return u"영"
    return num_kor_read(num)


if __name__ == "__main__":
    print(main())
