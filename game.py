import pygame
from gameparts import Board

pygame.init()

CELL_SIZE = 100
BOARD_SIZE = 3
WIDTH = HEIGHT = CELL_SIZE * BOARD_SIZE
LINE_WIDTH = 15
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
X_COLOR = (84, 84, 84)
O_COLOR = (242, 235, 211)
X_WIDTH = 25
O_WIDTH = 15
SPACE = CELL_SIZE // 4

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BG_COLOR)


def draw_lines():
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (0, CELL_SIZE * i),
            (WIDTH, CELL_SIZE * i),
            LINE_WIDTH
        )
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (CELL_SIZE * i, 0),
            (CELL_SIZE * i, HEIGHT),
            LINE_WIDTH
        )


def draw_figures(board):
    for row in range(BOARD_SIZE):
        for colum in range(BOARD_SIZE):
            if board[row][colum] == 'X':
                pygame.draw.line(
                    screen,
                    X_COLOR,
                    (colum * CELL_SIZE + SPACE, row * CELL_SIZE + SPACE),
                    (
                        colum * CELL_SIZE + CELL_SIZE - SPACE,
                        row * CELL_SIZE + CELL_SIZE - SPACE,
                    ),
                    X_WIDTH,
                )
                pygame.draw.line(
                    screen,
                    X_COLOR,
                    (
                        colum * CELL_SIZE + SPACE,
                        row * CELL_SIZE + CELL_SIZE - SPACE
                    ),
                    (
                        colum * CELL_SIZE + CELL_SIZE - SPACE,
                        row * CELL_SIZE + SPACE,
                    ),
                    X_WIDTH,
                )
            elif board[row][colum] == 'O':
                pygame.draw.circle(
                    screen,
                    O_COLOR,
                    (
                        colum * CELL_SIZE + CELL_SIZE // 2,
                        row * CELL_SIZE + CELL_SIZE // 2,
                    ),
                    CELL_SIZE // 2 - SPACE,
                    O_WIDTH,
                )


def save_result(result):
    with open('result.txt', 'a', encoding='UTF-8') as file:
        file.write(result + '\n')


def main():
    game = Board()
    current_palyer = 'X'
    running = True
    draw_lines()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX = event.pos[0]
                mouseY = event.pos[1]
                clicked_col = mouseX // CELL_SIZE
                clicked_row = mouseY // CELL_SIZE
                if game.board[clicked_row][clicked_col] == ' ':
                    game.make_move(clicked_row, clicked_col, current_palyer)
                    if game.check_win(current_palyer):
                        result = f'Player {current_palyer} wins!'
                        print(result)
                        save_result(result)
                        running = False
                    elif game.is_field_full():
                        result = 'Draw!'
                        print(result)
                        save_result(result)
                        running = False
                    current_palyer = 'O' if current_palyer == 'X' else 'X'
                    draw_figures(game.board)
        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()
