try:
    num1 = int(input("Введить перше число: "))
    num2 = int(input("Введить друге число: "))
    num3 = int(input("Введить третє число: "))
    operation = input("Введи 'max', 'min', or 'average': ")
    if operation == 'max':
        result = max(num1, num2, num3)
        print("Максимальна кількість:", result)
    elif operation == 'min':
        result = min(num1, num2, num3)
        print("Минімальна кількість:", result)
    elif operation == 'average':
        result = (num1 + num2 + num3) / 3
        print("Середнє арифметичне:", result)
    else:
        print("Введено неприпустиму операцію. Будь ласка, ведіть 'max', 'min', or 'average'.")
except Exception as ex:
    print(ex)