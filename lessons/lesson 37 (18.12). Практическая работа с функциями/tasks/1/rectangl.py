def rectangle_info(width, height):
    # TODO: проверка типа
    # TODO: проверка значения (> 0)
    # TODO: вычислить площадь
    # TODO: вычислить периметр
    # TODO: вернуть кортеж (площадь, периметр)
    pass
if not isinstance(width, int) or not isinstance(height, int):
    raise TypeError("width и height должны быть целыми числами")
if width <= 0 or height <= 0:
    raise ValueError("width и height должны быть больше нуля")
