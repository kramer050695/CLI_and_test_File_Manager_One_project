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


def find_files_in_dir(directory: str, pattern: str):
    regex = re.compile(pattern)
    matched_files = []

    for root, dirs, files in os.walk(directory):
        for filename in files:
            if regex.search(filename):
                matched_files.append(os.path.join(root, filename))

    return matched_files


def add_date_to_files(path: str, recursive=False):
    if os.path.isfile(path):
        _add_date_to_filename(path)

    elif os.path.isdir(path):
        if recursive:
            for root, dirs, files in os.walk(path):
                for filename in files:
                    file_path = os.path.join(root, filename)
                    _add_date_to_filename(file_path)
        else:
            for filename in os.listdir(path):
                file_path = os.path.join(path, filename)
                if os.path.isfile(file_path):
                    _add_date_to_filename(file_path)

def _add_date_to_filename(file_path: str):
    creation_time = os.path.getctime(file_path)
    date_str = datetime.fromtimestamp(creation_time).strftime('%Y%m%d')

    dir_name, filename = os.path.split(file_path)

    if date_str in filename:
        return

    new_filename = f"{date_str}_{filename}"

    new_path = os.path.join(dir_name, new_filename)

    os.rename(file_path, new_path)