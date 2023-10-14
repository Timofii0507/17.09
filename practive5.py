try:
    num1 = int(input("Введить перше число: "))
    num2 = int(input("Введить друге число: "))
    operation = input("Введіть 'sum', 'product', 'butchery' or 'arithmetic mean':")
    if operation == 'sum':
        result = num1 + num2
        print("Сума чисел дорівнює:", result)
    elif operation == 'product':
        result = num1 * num2
        print("Добуток чисел дорівнює:", result)
    elif operation == 'butchery':
        result = num1 - num2
        print("Різнриця чисел дорівнює:", result)
    elif operation == 'arithmetic mean':
        result = (num1 + num2)/2
        print("Середньоарифметичне чисел дорівнює:", result)
    else:
        print("Введено неприпустиму операцію. Будь ласка, введіть 'sum', 'product', 'butchery' or 'arithmetic mean'.")
except Exception as ex:
    print(ex)