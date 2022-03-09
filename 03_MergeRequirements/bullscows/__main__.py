import os.path
import sys
import urllib.request
from argparse import ArgumentParser
from locale import setlocale, LC_ALL

from bullscows import gameplay


def main(dictionary_path, length):
    # Установка русского языка в консоли
    setlocale(LC_ALL, ('ru_RU', 'UTF-8'))

    if dictionary_path is None:
        raise ValueError("Словарь должен быть обязательно указан. "
                         "Это может быть или путь к файлу на локальном компьютере, либо URL на файл в сети Интернет.")

    dictionary = get_dictionary(dictionary_path)
    # Фильтрация словаря по размеру слов
    filtered_dictionary = [word for word in dictionary if len(word) == length]

    print('Задана длина слов: {}. Слова иной длины будут игнорироваться.'.format(length))
    steps = gameplay(ask, inform, filtered_dictionary)
    print("Количество попыток: {}".format(steps))


def get_dictionary(dictionary_path):
    # Если по указанной директории на локальном комрьютере есть требуемый файл, то читаем его
    # Иначе лезем в Интернет
    return get_local_directory(dictionary_path) if os.path.exists(dictionary_path) \
        else get_Internet_dictionary(dictionary_path)


def get_Internet_dictionary(dictionary_path):
    # Прочтение файла из интернета
    with urllib.request.urlopen(dictionary_path) as url_file:
        return url_file.read().decode('utf-8').split()


def get_local_directory(dictionary_path):
    # Прочтение локального файла
    with open(dictionary_path) as dictionary_file:
        return dictionary_file.read().split()


def ask(prompt: str, valid: list[str] = None) -> str:
    while True:
        try:
            # Требуем ввод в консоли
            result = input(prompt)
            # Если результат из списка корректных слов, то обрабатываем его дальше
            if valid is None or result in valid:
                return result
            # Если слово какое-то странное
            elif valid and not result in valid:
                print("Введено слово не из словаря допустимых значений. Попробуйте еще раз.")
        except:
            # На случай Ctrl + C, если захочется выйти из программы
            sys.exit("Ошибка ввода")


def inform(format_string: str, bulls: int, cows: int) -> None:
    # Красивый принт с состоянием игры
    print(format_string.format(bulls, cows))


def get_args():
    # Инициализация аргументов для парсера в консоли
    parser = ArgumentParser()
    parser.add_argument('--dictionary', type=str)
    parser.add_argument('--length', type=int, default=5)

    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()

    main(dictionary_path=args.dictionary, length=args.length)
