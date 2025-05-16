import os
import shutil
import re
from datetime import datetime


def copy_file(source_path: str, destination_path: str):
    if not os.path.isfile(source_path):
        raise FileNotFoundError(f"Исходный файл не найден: {source_path}")
    shutil.copy2(source_path, destination_path)


def delete_path(path: str):
    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)
    else:
        raise FileNotFoundError(f"Путь не найден: {path}")


def count_files_in_dir(directory: str) -> int:
    total = 0
    for root, dirs, files in os.walk(directory):
        total += len(files)
    return total


def find_files_in_dir():
    pass


def add_date_to_files():
    pass


def _add_date_to_filename():
    pass