board = list(range(1,10))
wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (6, 4, 2)]
def field():
    print('_________')
    for i in range(3):
        print(board[0+i], '|', board[3+i], '|', board[6+i])
    print('_________')
def player_move(abc):
    while True:
        player = input(f'Введите клетку, ходит {abc} : ')
        if not (player.isdigit()):
            print('Введите число')
        elif int(player) > 9 or int(player) < 1:
            print('Введите допустимое значение')
        elif board[int(player)-1] in ('X', 'O'):
            print('Клетка уже занята')
        else:
            print(f'{abc} ходит на ячейку {player}')
            board[int(player)-1] = abc
            break
def wins_check(abc):
    for b in wins:
        if board[b[0]] == board[b[1]] == board[b[2]]:
            print(f'Победа игрока : {abc}')
            return False
    else:
        return True
def play():
    move = 9
    abc = 'X'
    while move > 0 and wins_check(abc):
        if move % 2 == 0:
            abc = 'O'
        else:
            abc = 'X'
        field()
        player_move(abc)
        move -= 1
    if move == 0 and wins_check(abc):
        print('Ничья')
    field()


play()


