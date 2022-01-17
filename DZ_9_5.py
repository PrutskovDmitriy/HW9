class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки {self.title}")


class Pen(Stationery):

    def draw(self):
        print(f'Ручка: {self.title}, пишет толщиной 0.7 {"-" * 20}')


class Pencil(Stationery):

    def draw(self):
        print(f'Карандаш: {self.title}, пишет толщиной 0.5 {"." * 20}')


class Handle(Stationery):
    def draw(self):
        print(f'Маркер: {self.title}, пишет толщиной 1.0 {"*" * 20}')


pen = Pen('Erich Crauze')
pen.draw()
print()
pencil = Pencil('Tukzar')
pencil.draw()
print()
handle = Handle('Berlingo')
handle.draw()
