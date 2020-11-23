from gobj import*

class Background:
    def __init__(self, file:str):
        self.file=file
        self.image=gfw.image.load(res(file))
        self.cw, self.ch = get_canvas_width(), get_canvas_height()
        self.speed=0

    def update(self):
        pass

    def draw(self):
        page = self.image.w * self.ch // self.image.h
        self.image.draw(600,300,1200,600)




