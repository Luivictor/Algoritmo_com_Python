def tipo_lado(self) -> str:
    side_name = ''
    sides = len(set(self.side_list()))

    if sides == 3:
        side_name = 'escaleno'
    elif sides == 2:
        side_name = 'isósceles'
    elif sides == 1:
        side_name = 'equilátero'

    return side_name