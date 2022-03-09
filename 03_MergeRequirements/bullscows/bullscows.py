from random import seed, choice

from textdistance import hamming, bag


def bullscows(guess: str, secret: str) -> (int, int):
    # https://en.wikipedia.org/wiki/Hamming_distance
    # Применяется расстояние Хэмминга (сколько букв надо изменить, чтоб слова стали идентичны)
    # Далее вычисляется длина слова - расстояние
    bulls = hamming.similarity(guess, secret)
    cows = bag.similarity(guess, secret) - bulls
    return bulls, cows


def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    if len(words) == 0:
        raise ValueError("Размер словаря равен 0. Невозможно создать игру")

    # Дефолтное состояние слова пользователя и количество его попыток
    guess = ''
    steps = 0

    # Случайным образом генерируем искомое слово
    seed()
    secret = choice(words)
    # Играем ровно до того момента, как слово не станет отгаданным
    while guess != secret:
        steps += 1
        # Собственно, реализованные ранее методы
        guess = ask("Введите слово: ", words)
        bulls, cows = bullscows(guess, secret)
        inform("Быки: {}, Коровы: {}", bulls, cows)
        # Если количество быков == длина искомого слова, то это победа
        if bulls == len(secret):
            return steps
