import pickle
import game_state_gameplay
from functools import reduce
import gfw
from pico2d import *

objects = []
trashcan = []

def init(layer_names):
    global objects
    objects = []
    gfw.layer = lambda: None
    layerIndex = 0
    for name in layer_names:
        objects.append([])
        gfw.layer.__dict__[name] = layerIndex
        layerIndex += 1

def add(layer_index, obj):
    objects[layer_index].append(obj)

def remove(obj):
    trashcan.append(obj)

def all_objects():
    for layer_objects in objects:
        for obj in layer_objects:
            yield obj

def object(layer_index, object_index):
    layer_objects = objects[layer_index]
    return layer_objects[object_index]

def objects_at(layer_index):
    for obj in objects[layer_index]:
        yield obj

def count_at(layer_index):
    return len(objects[layer_index])

def count():
    return reduce(lambda sum, a: sum + len(a), objects, 0)

def clear():
    global objects
    for o in all_objects():
        del o
    objects = []

def clear_at(layer_index):
    for o in objects[layer_index]:
        del o
    objects[layer_index] = []

def update():
    for obj in all_objects():
        obj.update()
    if len(trashcan) > 0:
        empty_trashcan()
    # counts = list(map(len, objects))
    # print('count:', counts, count())

def draw():
    for obj in all_objects():
        obj.draw()

def empty_trashcan():
    global trashcan

    for obj in trashcan:
        for layer_objects in objects:
            # if obj in layer_objects:
            #     layer_objects.remove(obj)
            try:
                layer_objects.remove(obj)
            except ValueError:
                pass
    trashcan = []

def save(fn='world.pickle'):
    with open(fn, 'wb') as f:
        pickle.dump(objects, f)

def load(fn='world.pickle'):
    global objects
    with open(fn, 'rb') as f:
        objects = pickle.load(f)

def collide(a, b):
    'left_a, bottom_a, right_a, top_a = a.get_bb()'
    'left_b, bottom_b, right_b, top_b = b.get_bb()'
    'if left_a > right_b: return False'
    'if right_a < left_b: return False'
    'if top_a < bottom_b: return False'
    'if bottom_a > top_b: return False'

    if a.returnType() == 0 and b == 0:
        if 500 - a.getYpoision() < 50:
            game_state_gameplay.LeftCollide = True
            return True
        else:
            return False

    elif a.returnType() == 1 and b == 1:
        if 500 - a.getYpoision() < 50:
            game_state_gameplay.UpCollide = True
            return True
        else:
            return False

    elif a.returnType() == 2 and b == 2:
        if 500 - a.getYpoision() < 50:
            game_state_gameplay.DownCollide = True
            return True
        else:
            return False

    elif a.returnType() == 3 and b == 3:
        if 500 - a.getYpoision() < 50:
            game_state_gameplay.RightCollide = True
            return True
        else:
            return False

    else:
        return False
