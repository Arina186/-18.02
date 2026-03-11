is_continue = True
while is_continue:
    print(" 1 - map числа в строку\n"
          " 2 - filter > 0\n"
          " 3 - filter палиндром\n"
          " 4 - площадь квартиры\n"
          " 5 - имт\n"
          " 6 - калькулятор\n"
          " 7 - фильтр фото\n"
          " 8 - exit\n")


    def get_int_input(prompt):
        while True:
            try:
                int_num = int(input(prompt))
                return int_num
            except ValueError:
                print("Введите целое число!")


    import time


    def repeat(n):
        def timer_decorator(func):
            def wrapper(*args, **kwargs):
                start_time = time.time()  # засекаем общее начало отсчета
                for sth in range(n):
                    func(*args, **kwargs)  # вызываем ф-цию n раз
                end_time = time.time()  # время конца
                average_time = (end_time - start_time) / n

                print(f"Среднее время выполнения функции {func.__name__} за {n} запусков: {average_time} сек ")
                return average_time

            return wrapper

        return timer_decorator


    user_choice = get_int_input("Enter action number: ")
    if user_choice == 1:
        sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        print(list(map(str, sequence)))

    elif user_choice == 2:
        @repeat(5)
        def some_task():
            sequence_two = [-10, -6, 7, 4, 2, -4, 7, 1, -15, -18, 17, 62]
            print(list(filter(lambda x: x > 0, sequence_two)))


        some_task()

    elif user_choice == 3:
        def is_palindrome(word):
            s = word.lower().replace(" ", "")
            return s == s[::-1]


        word = ["abccba", "hsdhee", "level", "fjkroeolel", "radar", "fjfkkk", "civic", "madam", "hffhfhfh"]
        print(list(filter(is_palindrome, word)))

    elif user_choice == 4:
        from functools import reduce

        rooms = [
            {"name": "Kitchen", "length": 6, "width": 4},
            {"name": "Room 1", "length": 5.5, "width": 4.5},
            {"name": "Room 2", "length": 5, "width": 4},
            {"name": "Room 3", "length": 7, "width": 6.3},
        ]
        separate_square = list(map(lambda x: x["length"] * x["width"], rooms))
        print(f"Площадь каждой комнаты: {separate_square} ")
        print(f"Общая площадь квартиры: ", reduce(lambda x, y: x + y, separate_square))

    elif user_choice == 5:

        try:
            cholesterol = float(input("Enter your level of cholesterol: "))
            sugar = float(input("Enter your level of sugar: "))
            bmi = float(input("Enter your bmi: "))
            systolic_blood_pressure = int(input("Enter your upper blood pressure: "))
            diastolic_blood_pressure = int(input("Enter your diastolic blood pressure: "))
            age = int(input("Enter your age: "))
            smoking = input("Do you smoke? (yes/no): ").lower() == "yes"
            elevated_count = 0  # счетчик количества отклонений по каждому показателю

            if cholesterol >= 5.2: elevated_count += 1
            if sugar >= 5.5: elevated_count += 1
            if bmi < 18.5 or bmi > 24.9: elevated_count += 1
            if systolic_blood_pressure > 130 or diastolic_blood_pressure > 85: elevated_count += 1
            severe_risk = (cholesterol > 6.5 or sugar > 7.0 or bmi > 30.0 or systolic_blood_pressure > 140
                           or diastolic_blood_pressure > 90)
            if bmi < 16 or bmi > 40:
                risk = "Special case: critical!"
            elif elevated_count >= 4 and smoking and age > 60:
                risk = "Critical"
            elif elevated_count >= 3 or severe_risk:
                risk = "High"
            elif 1 <= elevated_count <= 2 or age > 45:
                risk = "Moderate"
            else:
                risk = "Low"

            print(f"Test result: {risk}")

        except ValueError:
            print("Error: Please, enter only numbers! (for float numbers use a point).")
        except Exception as e:
            print(f"Occurred unexpected error: {e}")

    elif user_choice == 6:
        def calculator():
            print("Calculator")
            print("Enter 'exit' in order to leave")
            while True:
                try:
                    user_inp = input("\nEnter the first number: ")
                    if user_inp.lower() == 'exit': break
                    num_one = float(user_inp)
                    operation = input("Enter the operation(+, -, *, /): ")
                    if operation.lower() == 'exit': break
                    user_inp = input("Enter the second number: ")
                    if user_inp.lower() == 'exit': break
                    num_two = float(user_inp)
                    if operation == '+':
                        result = num_one + num_two
                    elif operation == '-':
                        result = num_one - num_two
                    elif operation == '*':
                        result = num_one * num_two
                    elif operation == '/':
                        result = num_one / num_two
                    else:
                        print("Error: Operation not supported!")
                        continue

                    print(f"Result: {num_one} {operation} {num_two} = {result}")

                except (ValueError, TypeError):
                    print("Error: Please, enter only numbers!")
                except ZeroDivisionError:
                    print("Error: You can't divide by zero!")
                except Exception as e:
                    print(f"Occurred unexpected error: {e}")


        calculator()

    elif user_choice == 7:
        from PIL import Image, ImageDraw


        def apply_vague_picture(image_path, block_size):  # output- это уже будет преобразованная картинка
            img = Image.open(image_path)  # откроется картинка
            pixels = img.load()  # загрузит все пиксели из картинки
            width, height = img.size  # тут скобок нет так как размер это характеристика а не действие
            result = Image.new("RGB", (width, height))
            draw = ImageDraw.Draw(result)
            for i in range(0, width, block_size):
                for j in range(0, height, block_size):
                    box = (i, j, min(i + block_size, width), min(j + block_size, height))
                    # Вырезаем кусочек и сжимаем его до 1 пикселя,
                    # чтобы Pillow сам посчитал средний цвет (метод BOX)
                    region = img.crop(box)
                    avg_colour = region.resize((1, 1), resample=Image.Resampling.BOX).getpixel((0, 0))
                    # Рисуем закрашенный квадрат этим цветом
                    draw.rectangle(box, fill=avg_colour)

            return result


        res = apply_vague_picture("landscape.webp", 6)
        res.show()
        res.save("pixel_landscape.jpg")


    elif user_choice == 8:
        print("До свидания!")
        is_continue = False
