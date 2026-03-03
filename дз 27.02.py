is_continue = True
while is_continue:
    print(" 1 - Рекурсия. Бинарный поиск\n"
          " 2 - Перевод из 10-ной системы счисления в 2-ную\n"
          " 3 - Простое ли число\n"
          " 4 - НОД\n"
          " 5 - Шифр Цезаря\n"
          " 6 - Шифр Виженера\n"
          " 7 - Сжатие строки\n"
          " 8 - Спам - фильтр\n"
          " 9 - Имитация «Генетического алгоритма»\n"
          "10 - Транслитератор\n"
          "11 - Поиск «Пиков» в списке\n"
          "12 - exit\n")


    def get_int_input(prompt):
        while True:
            try:
                int_num = int(input(prompt))
                return int_num
            except ValueError:
                print("Введите целое число!")


    user_choice = get_int_input("Enter action number: ")
    if user_choice == 1:
        def binary_search(numbers, left, right, goal):
            if left > right:
                return -1
            # принято возвращать -1, если функция должна вернуть индекс, но не смогла найти
            mid = (left + right) // 2
            if numbers[mid] == goal:
                return mid # возвращает индекс, а если было бы return numbers[mid] - вернуло бы само значение из списка
            elif numbers[mid] > goal:
                return binary_search(numbers, left, mid - 1, goal)
            else:
                return binary_search(numbers, mid + 1, right, goal)



        numbers = [1, 5, 7, 16, 23, 28, 31, 38, 42]
        print("List of numbers: ", numbers)
        goal = get_int_input("Enter the number from the list to be depicted: ")
        result = binary_search(numbers, 0, len(numbers) - 1, goal) # задаются лев и правая границы
        if result != -1:
            print(f"Element {goal} has an index: {result}")
        else:
            print("Element is not found. Try again!")

    elif user_choice == 2:
        def from_decimal_to_binary(number):
            binary_number = ""
            while number > 0:
                binary_number += str(number % 2)
                number //= 2
            return binary_number

        number = get_int_input("Enter a decimal number: ")
        result = from_decimal_to_binary(number)
        print(f"Your number {number} from decimal to binary system: {result}")






