import numpy as np
def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загадываем число. Defaults to 1.

    Returns:
        int: Число попыток
    """   
        
    count = 0 
    # Задаём левую и правую границу промежутка случайных чисел
    left_side = 1
    right_side = 101
    predict_number = np.random.randint(left_side, right_side) # Предпологаемое число
        
    while number != predict_number:
        count += 1
        # Если предпологаемое число меньше угадываемого,
        # предпологаемое число становится новой левой границей промежутка
        if number > predict_number:
            left_side = predict_number
            predict_number = np.random.randint(left_side, right_side)
        # Если предпологаемое число больше угадываемого,
        # предпологаемое число становится новой правой границей промежутка
        elif number < predict_number:
            right_side = predict_number + 1
            predict_number = np.random.randint(left_side, right_side)
        
    return count

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)