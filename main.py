try:
    num1 = int(input("Введить перше число: "))
    num2 = int(input("Введить друге число: "))
    num3 = int(input("Введить третє число: "))
    operation = input("Ведіть 'sum' or 'product':")
    if operation == 'sum':
        result = num1 + num2 + num3
        print("Сума чисел дорівнює:", result)
    elif operation == 'product':
        result = num1 * num2 * num3
        print("Добуток чисел дорівнює:", result)
    else:
        print("Введено неприпустиму операцію. Будь ласка, введіть 'sum' or 'product'.")
except Exception as ex:
    print(ex)