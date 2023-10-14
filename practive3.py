try:
    num1 = int(input("Введить перше число: "))
    num2 = int(input("Введить друге число: "))
    if num1 > num2:
        print("Максимум:", num1)
    elif num2 > num1:
        print("Максимум:", num2)
    else:
        print("Рівні")
except Exception as ex:
    print(ex)