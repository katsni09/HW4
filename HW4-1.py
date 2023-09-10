# 1. Користувач вводить рядок з клавіатури.
# Порахуйте кількість літер, цифр у рядку. Виведіть обидві кількості на екран. (використовувати цикл)

line = input()
count_letters = 0
count_digits = 0
for i in line:
    if i.isalpha():
        count_letters += 1
    elif i.isdigit():
        count_digits += 1
print(count_letters)
print(count_digits)
