# task 1
import os, platform

print(f"Operational system: {platform.system()} {os.name}")  # имя операционной системы
print(f"Current working directory: {os.getcwd()}")  # путь до текущей папки

current_files = os.listdir()

extensions = set()
for file in current_files:
    if file.count(".") == 1:
        file_parts = file.split(".")
        if file_parts[0] != "" and file_parts[1] != "":
            extensions.add(file_parts[1].lower())

print(extensions)
# сгруппировать файлы в папку
for ext in extensions:
    if ext != "py":
        new_folder_name = f"{ext}s"
        if not os.path.exists(new_folder_name):
            os.mkdir(new_folder_name)
        count = 0  # сколько файлов в папке
        total_size = 0  # для размера в гб
        for file in current_files:
            if file.count(".") == 1:
                file_parts = file.split(".")
                if file_parts[0] != "" and file_parts[1] != "" and file_parts[1] == ext:
                    file_path = os.path.join(os.getcwd(), file)
                    total_size += os.path.getsize(file_path)
                    count += 1
                    replaced_file_path = os.path.join(os.getcwd(), new_folder_name, file)  # file - новое имя файла
                    os.replace(file, replaced_file_path)
        if count > 0:
            size_file = total_size / 1024 ** 3
            print(f"В папке с {ext} файлами перемещено {count} файлов, их суммарный размер - {size_file:.10f} ГБ")
        # .5f где 5-кол-во знаков после запятой f — тип данных fixed-point (число с фиксированной точкой)
        else:
            print(f"Для расширения {ext} файлов не найдено (возможно, уже перемещены)")

target_file = "dhjddj.txt"
new_file = "poetry.txt"

if "." in target_file:
    ext = target_file.split(".")[-1]
    folder_of_file = f"{ext}s"
    old_path = os.path.join(os.getcwd(), folder_of_file, target_file)
    new_path = os.path.join(os.getcwd(), folder_of_file, new_file)
    # Проверяем наличие и переименовываем
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"File {target_file} was renamed to {new_file}")
    else:
        print(f"File {target_file} was not found in {folder_of_file}")

# task 3

input_path = os.path.join("txts", "text.txt")
output_path = os.path.join("txts", "output.txt")
try:
    with open(input_path, "r", encoding="utf-8") as file, open(output_path, "w", encoding="utf-8") as output:
        for line in file:
            word_count = line.lower().split()
            if not word_count:  # Если строка пустая — пропускаем
                continue
            counts = {}
            for word in word_count:
                clean_word = word.strip(".,!?;:-")
                if clean_word in counts:
                    counts[clean_word] += 1  # Если слово уже записано, мы просто увеличиваем число рядом с ним на +1.
                else:
                    counts[
                        clean_word] = 1  # Если слова еще нет, мы записываем его в книжку и ставим цифру 1, так как мы увидели его в первый раз.

            max_word = ""
            max_count = 0
            for word in counts:
                if counts[word] > max_count:
                    max_count = counts[word]
                    max_word = word
            output.write(f"{max_word} {counts[max_word]}\n")

except Exception as e:
    print(f"Error: {e}")

# task 4
input_path = os.path.join("txts", "forbidden_words.txt")
try:
    with open(input_path, "r", encoding="utf-8") as file:
        forbidden_words = file.read().lower().split()
    file_name = input("Enter the filename(another_text.txt): ")
    target = os.path.join("txts", file_name)
    with open(target, "r", encoding="utf-8") as file:
        text = file.read()

    for word in forbidden_words:
        word_len = len(word)
        stars = "*" * word_len
        # ищем где заменить в версии "нижнего регистра",
        # но замену делаем в оригинальном тексте
        index = text.lower().find(word)
        while index != -1:
            # Склеиваем текст: до найденного слова + звезды + после слова
            text = text[:index] + stars + text[index + word_len:]
            index = text.lower().find(word, index + word_len)
    print(f"Result: {text}")
except FileNotFoundError:
    print("File was not found")
except Exception as e:
    print(f"Error: {e}")

# task 5
input_path = os.path.join("txts", "student_grades.txt")
try:
    with open(input_path, "r", encoding="utf-8") as file:
        for line in file:
            data = line.split()
            if len(data) == 3 and data[2] < "3":
                print(f"Student {data[0]} {data[1]} got {data[2]}")
except Exception as e:
    print(f"Error: {e}")

# task 6
input_path = os.path.join("txts", "another_text.txt")
result = 0
current_num = ""
try:
    with (open(input_path, "r", encoding="utf-8") as file):
        text = file.read()
        for char in text:
            if char.isdigit():
                current_num += char
            else:
                if current_num:
                    result += int(current_num)  # Как только попадается НЕ цифра, превращаем накопленную строку в число
                    # и добавляем его в общую сумму
                    current_num = ""  # очищаем буфер, чтобы следующее число не приклеилось к предыдущему
        if current_num:  # Проверка, если файл заканчивается числом
            result += int(current_num)

        print(f"Total sum: {result}")
except Exception as e:
    print(f"Error: {e}")

# task 7
import string


def caesar_encyption(text, shift):
    encrypted_message = ""
    for char in text:
        if char.isalpha():
            is_russian = "а" <= char.lower() <= "я" or char.lower() == 'ё'
            if is_russian:
                alphabet_size = 33
                ru_alphabet = "абвгждеёзийклмнопрстуфхцчшщъыьэюя"
                if char.isupper():
                    ru_alphabet = ru_alphabet.upper()
                indx = ru_alphabet.find(char)
                encrypted_message += ru_alphabet[(indx + shift) % 33]
            else:
                alphabet_size = 26
                start = ord("A") if char.isupper() else ord("a")
                shifted_char = chr((ord(char) - start + shift) % alphabet_size + start)
                encrypted_message += shifted_char
        else:
            encrypted_message += char  # Символы и пробелы оставляем как есть
    return encrypted_message


if not os.path.exists("txts"):
    os.makedirs("txts")

input_path = os.path.join("txts", "for_caesar.txt")
output_path = os.path.join("txts", "final_caesar.txt")
try:
    with (open(input_path, "r", encoding="utf-8") as file):
        lines = file.readlines()
    with (open(output_path, "w", encoding="utf-8")) as file:
        for index, line in enumerate(lines, start=1):
            encrypted_line = caesar_encyption(line, index)  # Шаг шифра равен номеру строки (index)
            file.write(encrypted_line)
    print("Шифрование завершено успешно!")
except FileNotFoundError:
    print(f"Ошибка: Файл {input_path} не найден.")
except Exception as e:
    print(f"Error: {e}")

# task 8
is_continue = True
while is_continue:
    print(" 1 - преобразование в формат CSV\n"
          " 2 - сохранение данных в CSV-файл\n"
          " 3 - добавление информации о новом сотруднике в JSON-файл\n"
          " 4 - добавление информации о новом сотруднике в CSV-файл\n"
          " 5 - вывод информации о сотруднике по имени\n"
          " 6 - фильтр по языку\n"
          " 7 - фильтр по году\n"
          " 8 - exit\n")


    def get_int_input(prompt):
        while True:
            try:
                int_num = int(input(prompt))
                return int_num
            except ValueError:
                print("Enter only integer numbers!")


    def get_letter_input(prompt):
        while True:
            name = input(prompt).strip()
            # Убираем пробелы для проверки
            if name.replace(" ", "").isalpha() and len(name) > 0:
                return name
            else:
                print("Error! Name must contain only letters and cannot be empty")


    from datetime import datetime


    def get_birthday_input(prompt):
        while True:
            date_str = input(prompt).strip()
            try:
                # Пытаемся превратить строку в реальную дату по шаблону
                datetime.strptime(date_str, "%d.%m.%Y")
                return date_str
            except ValueError:
                print("Error: Use format: 11.08.2001 and enter a valid date!")


    def get_height_input(prompt):
        while True:
            try:
                hei = int(input(prompt))
                if 50 <= hei <= 250:
                    return hei
                else:
                    print("Height must be between 50cm and 250cm!")
            except ValueError:
                print("Enter only integer numbers!")


    def get_weight_input(prompt):
        while True:
            try:
                # Разрешаем вводить и точку, и запятую
                raw_val = input(prompt).replace(',', '.')
                val = float(raw_val)
                if 35.0 <= val <= 200.0:
                    return val
                else:
                    print("Weight must be between 35kg and 200kg!")
            except ValueError:
                print("Enter only numbers!")


    user_choice = get_int_input("Enter action number: ")
    import json
    import csv
    import os

    if user_choice == 1:
        def json_to_csv(input_path, output_path):
            with open(input_path, "r") as json_file:
                data = json.load(json_file)
            # Проверяем, что данные — это список объектов
            if not isinstance(data, list) or len(data) == 0:
                print("Error: JSON must contain a list of objects.")
                return
            # делаем список языков программирования в строку
            for item in data:
                if "languages" in item and isinstance(item["languages"], list):
                    item["languages"] = ", ".join(item["languages"])
                    # получаем заголовки
            head = data[0].keys()
            # записываем в cvs
            with open(output_path, "w", encoding='utf-8', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=head)
                writer.writeheader()
                writer.writerows(data)


        input_path = os.path.join("jsons", "employees.json")
        output_path = "employees.csv"
        json_to_csv(input_path, "employees.csv")

    elif user_choice == 2:
        def save_file_csv(input_path, output_path):
            with open(input_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                # Превращаем списки (например, languages) в строки через запятую
                for row in data:
                    for k, v in row.items():
                        if isinstance(v, list):
                            row[k] = ', '.join(map(str, v))
                with open(output_path, 'w', encoding='utf-8', newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=data[0].keys())
                    writer.writeheader()
                    writer.writerows(data)


        input_path = os.path.join("jsons", "employees.json")
        output_path = os.path.join("csvs", "employees.csv")
        save_file_csv(input_path, "employees.csv")

    elif user_choice == 3:
        def add_new_employee_to_json(input_path):
            if os.path.exists(input_path):
                with open(input_path, "r", encoding="utf-8") as file:
                    try:
                        data = json.load(file)
                    except json.JSONDecodeError:
                        data = []
            else:
                data = []

            print("--- Ввод данных нового сотрудника ---")
            name = get_letter_input("Enter employee's name and surname: ")
            birthday = get_birthday_input("Enter employee's birthday(for example: 11.08.2001): ")
            height = get_height_input("Enter employee's height(cm): ")
            weight = get_weight_input("Enter employee's weight(kg): ")
            car = get_letter_input("Does employee have a car? y/n: ")
            have_car = True if car == "y" else False
            languages = input("Enter employee's languages with commas: ")
            languages = languages.split(",")
            new_employee = {
                "name": name,
                "birthday": birthday,
                "height": height,
                "weight": weight,
                "car": have_car,
                "languages": languages
            }
            data.append(new_employee)
            with open(input_path, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
            print(f"Employee {name} is successfully added tot the file!")


        # ensure_ascii=False отвечает за то, как в JSON-файле будут выглядеть русские буквы,
        # записывает символы как есть
        input_path = os.path.join("jsons", "employees.json")
        add_new_employee_to_json(input_path)
