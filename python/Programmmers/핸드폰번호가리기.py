import re

phone_numbers = "01033334444"

print(phone_numbers[: len(phone_numbers) - 4])
tmp = phone_numbers[: len(phone_numbers) - 4]
print(re.sub(".", "*", tmp))

print(phone_numbers[-4:])
