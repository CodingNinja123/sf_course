import numpy as np
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict = np.random.randint(1,101)
    while number != predict:
        count+=1
        if number > predict: 
            predict += calculateNextPredictionAdjustment(predict, count) 
        elif number < predict: 
            predict -= calculateNextPredictionAdjustment(predict, count)
    return(count) # выход из цикла, если угадали

def calculateNextPredictionAdjustment(current, count):
    ''' Расчитывает число, на которое надо изменить predict переменную'''
    tmp = 0
    if current > 50:
        tmp = int((current - 50)/count)
    else:
        tmp = int((50 - current)/count)
    
    if(tmp > 0):
        return tmp
    return 1

        
score_game(game_core_v2)