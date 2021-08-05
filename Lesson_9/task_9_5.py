class Stationary:
    title = "some item"

    def draw(self):
        print(f"Hey, we are drawing with {self.title}")


class Pen(Stationary):
    title = "Pen"

    def draw(self):
        print('Its some real hard work - drawing with a pen')


class Pencil(Stationary):
    title = 'Pencil'

    def draw(self):
        print('Pencil is much better to texture your art')
        super().draw()


class Handle(Stationary):
    title = "Handle"

    def draw(self):
        print('Handle is junk')

base = Stationary()
pen = Pen()
pencil = Pencil()
handle = Handle()
base.draw()
pen.draw()
pencil.draw()
handle.draw()

