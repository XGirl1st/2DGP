from pico2d import *
import gfw
import arrow_generator
from background import Background
import time
from collections import OrderedDict
import random
import json
import arrow
import ending_state

canvas_width = 1200
canvas_height = 600

load_note = []
load_playtime = []
load_tempo = []
load_tempoTime = []
smallfont = None
now = 0
t = 0  # 변박 넘기기임 기억해라...

combo = 0
miss = 0
check = False
MaxC = 0

def enter():
   gfw.world.init(['bg', 'note'])
   global bg
   global load_note, load_playtime, load_tempo, load_tempoTime
   global leftTime, upTime, downTime, rightTime
   global now
   global combo
   global miss
   global check, miss_lifetime
   combo = 0
   now = 0

   global LeftCollide, RightCollide, UpCollide, DownCollide

   leftTime, upTime, downTime, rightTime = 0, 0, 0, 0
   LeftCollide = False
   RightCollide = False
   UpCollide = False
   DownCollide = False

   bg = Background('saber.jpg')
   gfw.world.add(gfw.layer.bg, bg)

   global music_bg
   music_bg = load_music('res/Dance till Dawn.mp3')
   music_bg.repeat_play()

   global music_playtime
   music_playtime = 0

   global black_left, black_up, black_down, black_right
   global slash_left, slash_down, slash_up, slash_right
   global HP

   black_left = gfw.image.load('res/black_left.png')
   black_up = gfw.image.load('res/black_up.png')
   black_down = gfw.image.load('res/black_down.png')
   black_right = gfw.image.load('res/black_right.png')

   slash_left = gfw.image.load('res/slash_left.png')
   slash_up = gfw.image.load('res/slash_up.png')
   slash_down = gfw.image.load('res/slash_down.png')
   slash_right = gfw.image.load('res/slash_right.png')

   HP = gfw.image.load('res/State.png')

   # JSON 읽어오는곳 :) 노트타입, 언제나오는지 시간도 있음
   with open('Note.json', 'r') as f:
      temp = json.load(f)
      t = temp["Note"]
      load_note = t
      t = temp["PlayTime"]
      load_playtime = t
      t = temp["Tempo"]
      load_tempo = t
      t = temp["TempoTime"]
      load_tempoTime = t


def update():
   global smallfont
   global bigfont
   global combo
   global MaxC


   global miss
   global check, miss_lifetime
   global LeftCollide, RightCollide, UpCollide, DownCollide
   global makenote, music_playtime, t, now
   # 노트를 만드는 부분 :)
   if music_playtime >= float(load_playtime[now]) and now + 1 < len(load_playtime):

      if load_playtime[now] == load_playtime[now + 1]:
         temp = now
         while load_playtime[temp] == load_playtime[temp + 1]:
            arrow_generator.create_arrow(load_note[temp], 300 + 200 * load_note[temp], 100, load_tempo[temp])
            if temp + 1 < len(load_playtime):
               temp += 1
         now = temp

      else:
         arrow_generator.create_arrow(load_note[now], 300 + 200 * load_note[now], 100, load_tempo[now])
         if now + 1 < len(load_playtime):
            now += 1

      # 리스트 초과하면 그냥 터질거임 예외처리 필수 :)
   music_playtime += gfw.delta_time

   if music_playtime >= 118:
      gfw.change(ending_state)
      return

   if music_playtime >= float(load_tempoTime[t]):
      if t + 1 < len(load_tempoTime):
         t += 1

   if time.time() - leftTime > 0.1:
      LeftCollide = False
   if time.time() - upTime > 0.1:
      UpCollide = False
   if time.time() - downTime > 0.1:
      DownCollide = False
   if time.time() - rightTime > 0.1:
      RightCollide = False

   gfw.world.update()

   for object in gfw.world.objects_at(gfw.layer.note):
      if object.checking():
         comboReset()
         gfw.world.remove(object)
         miss += 1
         check = True
         miss_lifetime = 0.5


def draw():
   global smallfont, bigfont, check, miss_lifetime

   gfw.world.draw()
   if LeftCollide:
      slash_left.draw(300, 500, 100, 100)
   else:
      black_left.draw(300, 500, 100, 100)

   if UpCollide:
      slash_up.draw(500, 500, 100, 100)
   else:
      black_up.draw(500, 500, 100, 100)

   if DownCollide:
      slash_down.draw(700, 500, 100, 100)
   else:
      black_down.draw(700, 500, 100, 100)

   if RightCollide:
      slash_right.draw(900, 500, 100, 100)
   else:
      black_right.draw(900, 500, 100, 100)

   HP.clip_draw_to_origin(0, 0, HP.w, int(HP.h - miss * HP.h / 50), 1050, 50)

   if miss == 50:
      gfw.change(ending_state)


   if smallfont == None:
      smallfont = load_font('ENCR10B.TTF', 70)

   smallfont.draw(10, 300, "Combo", (255, 255, 255))
   smallfont.draw(90, 220, "%d" % combo, (255, 255, 255))

   if check and miss_lifetime > 0:
      smallfont.draw(10, 100, "Miss", (255, 255, 255))
      miss_lifetime -= gfw.delta_time


def handle_event(evt):
   global leftTime, upTime, downTime, rightTime
   global LeftCollide
   global combo
   global miss
   global MaxC

   if evt.type == SDL_QUIT:
      gfw.quit()
   elif evt.type == SDL_KEYDOWN:
      if evt.key == SDLK_ESCAPE:
         gfw.pop()

      if evt.key == SDLK_LEFT:
         for game_object in gfw.world.objects_at(gfw.layer.note):
            if gfw.world.collide(game_object, 0):
               leftTime = time.time()
               gfw.world.remove(game_object)
               if MaxC <= combo:
                  MaxC += 1
               combo += 1

      if evt.key == SDLK_UP:
         for game_object in gfw.world.objects_at(gfw.layer.note):
            if gfw.world.collide(game_object, 1):
               upTime = time.time()
               gfw.world.remove(game_object)
               if MaxC <= combo:
                  MaxC += 1
               combo += 1

      if evt.key == SDLK_DOWN:
         for game_object in gfw.world.objects_at(gfw.layer.note):
            if gfw.world.collide(game_object, 2):
               downTime = time.time()
               gfw.world.remove(game_object)
               if MaxC <= combo:
                  MaxC += 1
               combo += 1

      if evt.key == SDLK_RIGHT:
         for game_object in gfw.world.objects_at(gfw.layer.note):
            if gfw.world.collide(game_object, 3):
               rightTime = time.time()
               gfw.world.remove(game_object)
               if MaxC <= combo:
                  MaxC += 1
               combo += 1


   elif evt.type == SDLK_UP:
      arrow_generator.create_arrow(0, 100, 100)


def comboReset():
   global combo
   global MaxC
   combo = 0


def missReset():
   global miss
   miss = 0

def Rank():
   global rank

   if miss<50:
      if (MaxC > 150):
         rank = 'S'
      elif (MaxC > 100):
         rank = 'A'
      elif (MaxC > 60):
         rank = 'B'
      elif (MaxC > 30):
         rank = 'C'
      elif (MaxC > 10):
         rank = 'D'
      else:
         rank = 'Fail'

   else: rank= 'Fail'






def exit():
   gfw.world.remove(bg)
   music_bg.stop()


if __name__ == '__main__':
   gfw.run_main()