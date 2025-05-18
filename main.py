import argparse
import sys
from operations import (
    copy_file,
    delete_path,
    count_files_in_dir,
    find_files_in_dir,
    add_date_to_files
)

def main():
    parser = argparse.ArgumentParser(description="Файловый менеджер")
    subparsers = parser.add_subparsers(dest='command', required=True)

    parser_copy = subparsers.add_parser('copy', help='Копировать файл')
    parser_copy.add_argument('source', help='Путь к исходному файлу')
    parser_copy.add_argument('destination', help='Путь к целевому файлу')

    parser_delete = subparsers.add_parser('delete', help='Удалить файл или папку')
    parser_delete.add_argument('path', help='Путь к файлу или папке')

    parser_count = subparsers.add_parser('count', help='Подсчитать файлы в папке')
    parser_count.add_argument('directory', help='Путь к папке')

    parser_find = subparsers.add_parser('find', help='Найти файлы по шаблону')
    parser_find.add_argument('directory', help='Путь к папке')
    parser_find.add_argument('pattern', help='Регулярное выражение для поиска')

    # add_date команда
    parser_date = subparsers.add_parser('add_date', help='Добавить дату в название файла')
    parser_date.add_argument('path', help='Путь к файлу или папке')
    parser_date.add_argument('--recursive', action='store_true', help='Обрабатывать все вложения')

    args = parser.parse_args()

    try:
        if args.command == 'copy':
            copy_file(args.source, args.destination)
            print(f"Файл скопирован: {args.source} -> {args.destination}")
        elif args.command == 'delete':
            delete_path(args.path)
            print(f"Удалено: {args.path}")
        elif args.command == 'count':
            count = count_files_in_dir(args.directory)
            print(f"Общее количество файлов: {count}")
        elif args.command == 'find':
            results = find_files_in_dir(args.directory, args.pattern)
            print("Найденные файлы:")
            for file in results:
                print(file)
        elif args.command == 'add_date':
            add_date_to_files(args.path, recursive=args.recursive)
            print("Дата добавлена успешно.")
        else:
            print("Неизвестная команда")
            sys.exit(1)
    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()