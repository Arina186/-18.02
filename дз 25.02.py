is_continue = True
while is_continue:
    print(" 1 - Генерация матрицы\n"
          " 2 - min и max в матрице\n"
          " 3 - Сумма всех элементов в матрице\n"
          " 4 - Умножение элементов с K столбцом\n"
          " 5 - Сумма элементов строки матрицы\n"
          " 6 - Поиск числа Н в столбцах матрицы\n"
          " 7 - Матрица из 0 и 1 + добавление столбца\n"
          " 8 - exit\n")


    def get_int_input(prompt):
        while True:
            try:
                int_num = int(input(prompt))
                return int_num
            except ValueError:
                print("Введите целое число!")


    user_choice = input("Enter action number: ")
    if user_choice == '1':
        from random import randint


        def generate_random_matrix(rows_count, columns_count):
            matrix = []
            for row in range(0, rows_count):
                matrix.append([])
                for col in range(0, columns_count):
                    matrix[row].append(randint(0, 50))

            return matrix


        def show_matrix(matrix):
            for row in matrix:
                print(row)

            return matrix

        rows_number = get_int_input("Enter rows number: ")
        columns_number = get_int_input("Enter columns number: ")
        result = generate_random_matrix(rows_number, columns_number)
        print(f" \nВаша матрица:")
        show_matrix(result)


