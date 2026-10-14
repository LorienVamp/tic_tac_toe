class FieldIndexError(IndexError):
    """Выбрасывается если выбрано знгачение вне поля."""

    def __init__(
            self,
            message='Введено значение за границами игрового поля!'
            ):
        super().__init__(message)


class CellOccupiedError(Exception):
    """Выбрасывается если игрок пытается занять уже занятую ячейку"""

    def __init__(
            self,
            messange='Попытка изменить занятую ячейку'
            ):
        super().__init__(messange)
