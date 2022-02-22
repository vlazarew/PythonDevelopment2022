from argparse import ArgumentParser
from locale import setlocale, LC_ALL

from figdate import date


def args_from_common_parser():
    # Инициализация аргументов для парсера в консоли
    parser = ArgumentParser()
    parser.add_argument('--format', type=str, default='%Y %d %b, %A')
    parser.add_argument('--font', type=str, default='graceful')

    return parser.parse_args()


def main(print_format, font):
    # Установка русского языка в консоли
    setlocale(LC_ALL, ('ru_RU', 'UTF-8'))
    # Принт метода из figdate
    print(date(print_format, font))


if __name__ == '__main__':
    args = args_from_common_parser()
    # Вызов основного метода
    main(print_format=args.format, font=args.font)
