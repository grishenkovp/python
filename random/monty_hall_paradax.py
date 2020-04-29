import random
import pandas as pd
# Первый игрок никогда не меняет своего первоначального мнения
player1 = []
# Второй игрок всегда выбирает другую дверь после открытия
player2 = []
doors = []
for round_game in range(0, 10):
    # Игрок делает своё первоначальное предположение
    choice_player = random.randint(0, 2)
    # Заполняем все двери козами
    for x in range(0, 3):
        doors.append('goat')
    # Случайным образом определяем дверь, где будет машина
    door_number_avto = random.choice([0, 1, 2])
    #  Помещаем туда авто
    doors[door_number_avto] = 'avto'
    # Фиксируем результаты двух игроков
    player1.append(doors[choice_player])
    if doors[choice_player] == 'avto':
        player2.append('goat')
    else:
        player2.append('avto')
df = pd.DataFrame({'player1': player1, 'player2': player2})
df = pd.melt(df)
df.columns = ['player', 'choice']
df_group = df.groupby(by=['player', 'choice']).size()
print(df_group)
