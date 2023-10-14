try:
    distance_meters = float(input("Введіть відстань у метрах: "))
    unit = input("Введіть 'miles', 'inches', or 'yards': ")
    if unit == 'miles':
        distance_miles = distance_meters / 1609.34
        print(distance_meters, "meters is equal to", distance_miles, "miles.")
    elif unit == 'inches':
        distance_inches = distance_meters * 39.37
        print(distance_meters, "meters is equal to", distance_inches, "inches.")
    elif unit == 'yards':
        distance_yards = distance_meters * 1.094
        print(distance_meters, "meters is equal to", distance_yards, "yards.")
    else:
        print("Введена неправильна одиниця виміру. Будь ласка, введіть 'miles', 'inches', or 'yards'.")
except Exception as ex:
    print(ex)