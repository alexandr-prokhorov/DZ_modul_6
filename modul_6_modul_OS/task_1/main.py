# Для выполнения данного задания я настоятельно рекомендую
# создать абсолютно новый проект.
# В этом проекте вам необходимо создать 2 папки а в каждой из
# них по 2 файла формата .txt:
# data_path_1 файлы внутри test_file_1.txt, test_file_2.txt;
# data_path_2 файлы внутри test_file_3.txt, test_file_4.txt.
# В корневой папке проекта вам необходимо создать файл
# main.py
# В этом файле вам необходимо написать код, который должен
# выполнять следующие задачи;
# Указать в консоли нормализованный абсолютный путь к
# файлу test_file_1.txt
# 1.
# При помощи функции os.walk() вывести в консоль
# содержимое папки вашего нового проекта
# 2.
# При помощи метода os.path.join() cоставить
# нормализованный абсолютный путь к файлу
# test_file_3.txt
# 3.
# Написать код для создания и для удаления папки внутри
# папки data_path_2

import os

file_1_path = os.path.abspath("data_path_1/test_file_1.txt")
print("нормализованный абсолютный путь к файлу test_file_1.txt:", file_1_path)
print()
print("Содержимое проекта")
for dir_path, dir_names, filenames in os.walk("."):
    print(f"Папка: {dir_path}")
    for dir_name in dir_names:
        print(f" Подпапка: {dir_name}")
    for filename in filenames:
        print(f" файл: {filename}")
print()
file_3_path = os.path.abspath(os.path.join('data_path_2/test_file_3.txt'))
print("нормализованный абсолютный путь к файлу test_file_3.txt:", file_3_path)

new_folder_path = os.path.join("data_path_2", "new_folder")

os.makedirs(new_folder_path)
print(f"папка создана: {new_folder_path}")
print()

os.rmdir(new_folder_path)
print(f"папка удалена: {new_folder_path}")



