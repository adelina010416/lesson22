# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:
    def __init__(self, field, state: str, speed: int):
        self.field = field
        self.state = state
        self.speed = speed

    def move(self, x_coord: int, y_coord: int, direction: str):
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

#     ...
