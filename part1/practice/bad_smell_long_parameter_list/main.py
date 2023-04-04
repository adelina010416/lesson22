# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def __init__(self, field, state, speed):
        self.field = field
        self.state = state
        self.speed = speed

    def move(self, x_coord, y_coord, direction):
        speed = self.get_speed()
        if direction == 'UP':
            new_y = y_coord + speed
            new_x = x_coord
        elif direction == 'DOWN':
            new_y = y_coord - speed
            new_x = x_coord
        elif direction == 'LEFT':
            new_y = y_coord
            new_x = x_coord - speed
        elif direction == 'RIGTH':
            new_y = y_coord
            new_x = x_coord + speed

        self.field.set_unit(x=new_x, y=new_y, unit=self)

    def get_speed(self):
        if self.state == "fly":
            self.speed *= 1.2
        elif self.state == "crawl":
            self.speed *= 0.5
        else:
            raise ValueError('Эк тебя раскорячило!')
