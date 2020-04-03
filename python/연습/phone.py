# def create_phone_number(string):
#     string = list(map(str, string))
#     head = "(%s) " % ("".join(string[:3]))
#     mid = "".join(string[3:6]) + "-"
#     end = "".join(string[6:])

#     return head + mid + end


def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
