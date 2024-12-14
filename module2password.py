def password(number):
    pass1 = ""
    for i in range(1, number):
        for j in range(i + 1, number):
            if number % (i + j) == 0:
                pass1 += str(i) + str(j)
    return pass1

print('Введите число для подбора пароля: ')
print(password(int(input())))