# CLI_and_test_File_Manager_One_project
Файловый менеджер на Python, который включает функции: разделение по модулям, обработку аргументов командной строки, тесты

Использование:
Запускать из командной строки:
python main.py <команда> [параметры]

### Команды и параметры
1) `copy` - Копировать файл или папку - `<source_path> <destination_path>`
2) `delete` - Удалить файл или папку - `<path>`
3) `count` - Подсчитать количество файлов в папке -`<directory>`
4) `find` - Найти файлы по шаблону - `<directory> <pattern>`
5) `add_date` - Добавить дату к именам файлов (рекурсивно или нет) - 
 - `<path> [--recursive]`

### Примеры использования

# Копирование файла
python main.py copy 1.txt copy_1.txt

# Удаление папки или файла
python main.py delete 1.txt

# Подсчет файлов в папке
python main.py count folder/

# Поиск файлов по шаблону *.txt в папке
python main.py find folder/ "*.txt"

# Добавление даты к файлам в папке (рекурсивно)
python main.py add_date folder/ --recursive
