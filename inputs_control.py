import pygame

class Button:
    def __init__(self, x, y, w, h, name):
        self.x, self.y=x, y #position
        self.w, self.h=w, h
        self.name=name
        self.area=pygame.Rect(self.x, self.y, self.w, self.h)
        self.clicked=False

    def mouse_input(self, ms_x, ms_y):
        if self.area.collidepoint(ms_x, ms_y):
            match self.name:
                case _: pass
