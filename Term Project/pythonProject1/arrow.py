from pico2d import*
import gobj
import gfw
import game_state_gameplay


PATH = [
    'res/ddr_left_arrow.png',
    'res/ddr_up_arrow.png',
    'res/ddr_down_arrow.png',
    'res/ddr_right_arrow.png'
]

class Arrow:
    def __init__(self, type: int, x, y, Tempo):
        self.x, self.y = x, y
        fn = PATH[type]
        self.images = gfw.image.load(fn)
        self.time = 0
        self.type = type
        self.tempo = Tempo
        self.speed=300
        self.width=100
        self.height=100

    def update(self):
        self.y += self.speed*gfw.delta_time*self.tempo



    def getYpoision(self):
        return self.y

    def checking(self):
        if self.y > get_canvas_height() + self.height // 2:
            return True
        else:
            return False

    def returnType(self):
        return self.type

    def draw(self):
        self.images.draw(self.x, self.y, self.width, self.height)

    def remove(self):
        gfw.world.remove(self)


