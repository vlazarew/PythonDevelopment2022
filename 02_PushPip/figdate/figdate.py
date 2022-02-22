from time import strftime

from pyfiglet import figlet_format


def date(print_format, font):
    # Используем figlet для получения текста
    # По формату получаем дату в соотствии с форматом, а также указываем шрифт
    return figlet_format(text=strftime(print_format), font=font)
