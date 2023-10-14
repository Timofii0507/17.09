try:
    num1 = int(input("Введить перше число: "))
    num2 = int(input("Введить друге число: "))
    maximum = max(num1, num2)
    print(f"Максимум із {num1} і {num2} - це {maximum}")
except Exception as ex:
    print(ex)