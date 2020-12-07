from pico2d import*
from arrow import Arrow

import gfw
import random

def create_arrow(a,x,y, temp):
    arrow=Arrow(a,x,y,temp)
    gfw.world.add(gfw.layer.note,arrow)


