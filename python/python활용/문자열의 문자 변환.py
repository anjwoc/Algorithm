def disemvowel(string):
    # table = string.maketrans("aeiouAEIOU", None)
    return string.translate(None, "aeiou")


import re


def disemvowel(string):
    return re.sub("[aeiou]", "", string, flags=re.IGNORECASE)


string = "this syntax is very useful"
a = disemvowel(string)
print(a)
