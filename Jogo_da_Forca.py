import random

def print_board(board):
    """Imprime o tabuleiro do jogo da velha."""
    print("-------------")
    for row in board:
        print("|", end="")
        for cell in row:
            print(f" {cell} |", end="")
        print("\n-------------")

def check_win(board, player):
    """Verifica se o jogador 'player' venceu."""

    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
   
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def check_draw(board):
    """Verifica se o jogo terminou em empate."""
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def get_human_move(board):
    """Obtém a jogada do jogador humano."""
    while True:
        try:
            row, col = map(int, input("Digite a posição (linha, coluna): ").split(","))
            if 1 <= row <= 3 and 1 <= col <= 3 and board[row - 1][col - 1] == " ":
                return row - 1, col - 1
            else:
                print("Posição inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite dois números separados por vírgula.")

def get_computer_move(board):
    """Obtém a jogada do computador."""
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
            return row, col

def play_game():
    """Executa o jogo da velha."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Bem-vindo ao Jogo da Velha!")
    print_board(board)

    while True:
        if current_player == "X":
            row, col = get_human_move(board)
        else:
            row, col = get_computer_move(board)

        board[row][col] = current_player
        print_board(board)

        if check_win(board, current_player):
            print(f"Parabéns, jogador {current_player}! Você venceu!")
            break
        elif check_draw(board):
            print("O jogo terminou em empate.")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()
