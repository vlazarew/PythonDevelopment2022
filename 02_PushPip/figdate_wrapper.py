import os
import subprocess
import venv
from argparse import ArgumentParser
from tempfile import TemporaryDirectory


def args_from_common_parser():
    # Инициализация аргументов для парсера в консоли
    parser = ArgumentParser()
    parser.add_argument('--format', type=str, default='%Y %d %b, %A')
    parser.add_argument('--font', type=str, default='graceful')

    return parser.parse_args()


if __name__ == '__main__':
    args = args_from_common_parser()

    with TemporaryDirectory() as venv_directory:
        # Создаём чистое venv-окружение во временном каталоге, с pip-ом (параметр with_pip)
        venv.create(venv_directory, with_pip=True)
        # Путь, по которому расположен pip
        pip_path = os.path.join(venv_directory, 'bin/pip')
        # Путь, по которому расположен python3
        python_path = os.path.join(venv_directory, 'bin/python3')

        # Установка пакета pyfiglet
        subprocess.run([pip_path, 'install', 'pyfiglet'])
        # Запуск программы будто через консоль
        subprocess.run([python_path, '-m', 'figdate', '--format', args.format, '--font', args.font])
