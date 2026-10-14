from gameparts import Board
from gameparts.exceptions import CellOccupiedError, FieldIndexError


def save_result(result):
    with open('result.txt', 'a', encoding='UTF-8') as file:
        file.write(result + '\n')


def main():
    game = Board()
    current_palyer = 'X'
    running = True
    game.display()
    while running:
        while True:
            try:
                row = int(input('Введите номер строки ')) - 1
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                colum = int(input('Введите номер столбца ')) - 1
                if colum < 0 or colum >= game.field_size:
                    raise FieldIndexError
                if game.board[row][colum] != ' ':
                    raise CellOccupiedError
            except FieldIndexError:
                print(f'Значения должно быть от 1 до {game.field_size}.')
                print('Пожалуйста снова введите значения для строки и стобца')
                continue
            except CellOccupiedError:
                print('Ячейка занята')
                print('Введите другие координаты')
            except ValueError:
                print('Буквы вводить нельзя, только числа')
                print('Пожалуйста снова введите значения для строки и стобца')
                continue
            except Exception as e:
                print(f'Возникла ошибка {e}')
                continue
            else:
                break
        game.make_move(row, colum, current_palyer)
        game.display()
        if game.check_win(current_palyer):
            result = f'Победили {current_palyer}'
            print(result)
            save_result(result)
            running = False
        if game.is_field_full():
            result = 'Ничья'
            print(result)
            save_result(result)
            running = False
        current_palyer = 'O' if current_palyer == 'X' else 'X'


if __name__ == '__main__':
    main()
