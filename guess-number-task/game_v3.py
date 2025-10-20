import numpy as np

def random_predict(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    #Присваиваем предполагаемому числу значение равное середине интервала
    predict_number = 50
    #Интервал для поиска
    interval_length = 50
    while True:
          count += 1
          if number == predict_number:
             break  # выход из цикла если угадали
          #Если интервал для поиска 1 и число не угадано, 
          # то сравниваем с угадываемым числом и проверяем соответственно следующее или предыдущее число
          elif (interval_length == 1) and (number != predict_number):
            if number > predict_number:
               predict_number += 1
            elif number < predict_number:
               predict_number -= 1
          #Уменьшаем длину интервала для поиска в два раза 
          # и изменяем предполагаемое число на длину этого интервала
          else:
            if number > predict_number:
              interval_length = interval_length//2
              predict_number = predict_number + interval_length
            elif number < predict_number:
              interval_length = interval_length//2
              predict_number = predict_number - interval_length
    return count
def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score

if __name__ == "__main__":
    # RUN
    score_game(random_predict)