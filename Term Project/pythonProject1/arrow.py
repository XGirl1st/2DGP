from pico2d import*
import gobj
import gfw



PATH = [
    'res/ddr_left_arrow.png',
    'res/ddr_up_arrow.png',
    'res/ddr_down_arrow.png',
    'res/ddr_right_arrow.png'
]

class Arrow:
    def __init__(self, type: int, x, y):
        self.x, self.y = x, y
        fn = PATH[type]
        self.images = gfw.image.load(fn)
        self.time = 0
        self.type = type

        self.speed=300
        self.width=100
        self.height=100

    def update(self):
        self.y += self.speed*gfw.delta_time

        if self.y > get_canvas_height() + self.height // 2:
            self.remove()

    def getYpoision(self):
        return self.y

    def returnType(self):
        return self.type

    def draw(self):
        self.images.draw(self.x, self.y, self.width, self.height)

    def remove(self):
        gfw.world.remove(self)


