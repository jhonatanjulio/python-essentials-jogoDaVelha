"""
Projeto Final: Jogo da Velha
Maratona Fundamentos de Python 1 - Cisco Skills for All
(Código desenvolvido por um iniciante em programação, portanto podem existir muitos erros)
Desenvolvido por: Jhonatan Julio
"""

from random import randint

board = list()
pos_row = int()
pos_move = int()


def display_game():  # Imprime a interface do status atual do tabuleiro
    print(f'''+-------+-------+-------+
|       |       |       |
|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
|       |       |       |
+-------+-------+-------+''')


def free_moves():  # Verifica quais são as casas do board ainda disponíveis para jogar e retorna a lista remaining_moves
    remaining_moves = []
    for gaps in range(len(board)):
        for moves in board[gaps]:
            if moves != 'X' and moves != 'O':
                remaining_moves.append(moves)
    if not remaining_moves:
        return None
    else:
        return remaining_moves


def find_index(move):  # Verifica e retorna a posição da jogada escolhida na função enter_move()
    global pos_row
    global pos_move
    for rows in range(len(board)):
        if move in board[rows]:
            pos_row = rows
            pos_move = board[rows].index(move)
            break


def enter_move():  # Entrada da jogada escolhida pelo usuario, e atualização no tabuleiro board
    print('Sua vez!')

    while True:
        try:
            move = int(input('Digite o número da posição que você deseja jogar: '))
            if move > 0 and move < 10:
                if move in free_moves():
                    find_index(move)
                    del board[pos_row][pos_move]
                    board[pos_row].insert(pos_move, 'O')
                    print(f'\nVocê jogou na posição {move}!\n')
                    display_game()
                else:
                    print('Você não pode jogar em uma lacuna já preenchida!')
                    return enter_move()
            else:
                print("Jogada inválida!")
                return enter_move()
            break
        except ValueError:
            print('Entrada inválida! Insira novamente.')

    who_win()


def computer_move():  # Jogada do computador (aleatória), e atualização no tabuleiro board
    move = randint(1, 9)
    if move not in free_moves():
        return computer_move()
    find_index(move)
    del board[pos_row][pos_move]
    board[pos_row].insert(pos_move, 'X')
    print(f'\nVez do computador!\nO computador jogou na posição {move}!\n')
    who_win()


def who_win():  # Verifica se a partida empatou, ou quem ganhou a partida e finaliza a sessão
    win_o = '\nParabéns! Você ganhou!\nFinalizando sessão...'
    win_x = 'Você perdeu!\nFinalizando sessão...'

    for rows in range(3):  # Linhas
        if board[rows][0] == board[rows][1] == board[rows][2]:
            if board[rows][0] == 'O':
                print(win_o)
            else:
                print(win_x)
            main()

    for columns in range(3):  # Colunas
        if board[0][columns] == board[1][columns] == board[2][columns]:
            if board[0][columns] == 'O':
                print(win_o)
            else:
                print(win_x)
            main()

    if board[0][0] == board[1][1] == board[2][2]:  # Diagonais
        if board[0][0] == 'O':
            print(win_o)
        else:
            print(win_x)
        main()

    if board[2][0] == board[1][1] == board[0][2]:  # Diagonais
        if board[2][0] == 'O':
            print(win_o)
        else:
            print(win_x)
        main()

    if free_moves() is None:  # OBS: se return None = O jogo ainda não acabou ; se return True = O jogo acabou Velha
        print("\nDeu velha!\nFinalizando sessão...")
        main()


def main():  # Função principal: menu do jogo e declaração do board
    global board
    board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]

    print("\n\nBem vindo ao Jogo da Velha!\nO computador é o \"X\" e você é o \"O\"\nO computador começa!\n")

    while True:
        try:
            inpt = int(input('[1] Jogar\n[2] Sair\n-> '))
            while not inpt > 0 or not inpt < 3:
                print('Entrada inválida! Insira novamente.')
                inpt = int(input('[1] Jogar\n[2] Sair\n-> '))
            if inpt == 2:
                print('Saindo...')
                exit()
            break
        except ValueError:
            print('Entrada inválida! Insira novamente.')

    while who_win() is None:
        display_game()
        enter_move()
        computer_move()


main()
