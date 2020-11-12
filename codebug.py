# To run this code on CodeBug, visit:
#
#     http://www.codebug.org.uk/learn/activity/66/tethering-codebug-with-python/#step585
#
import codebug_tether
from codebug_tether import (IO_DIGITAL_OUTPUT,
                            IO_DIGITAL_INPUT)
from codebug_tether.sprites import Sprite
from codebug_tether.sprites import StringSprite
import time

codebug = codebug_tether.CodeBug()
codebug.set_leg_io(0, IO_DIGITAL_INPUT);
codebug.set_leg_io(1, IO_DIGITAL_INPUT);
codebug.set_leg_io(2, IO_DIGITAL_INPUT);
codebug.set_leg_io(3, IO_DIGITAL_INPUT);
codebug.set_leg_io(4, IO_DIGITAL_INPUT);
codebug.set_leg_io(5, IO_DIGITAL_INPUT);
codebug.set_leg_io(6, IO_DIGITAL_INPUT);
codebug.set_leg_io(7, IO_DIGITAL_INPUT);

def build_sprite(rows):
  s = Sprite(5, 5)
  for i in range(5):
    s.set_row(i, rows[i])
  return s


string = "B&O er nice"
letter = 1
pressed = False
string = string.replace(" ","")
codebug.draw_sprite(0,0,StringSprite(string[0]))
while True:
    if codebug.get_input('A') == 1 and pressed == False:
        pressed = True

        codebug.draw_sprite(0,0,StringSprite(string[letter]))
        letter += 1
        if letter == (len(string)):
            letter = 0

    elif codebug.get_input('A') == 0:
        pressed = False 

    if codebug.get_input('B') == 1:
        codebug.draw_sprite(0, 0, build_sprite([0b00000,0b00000,0b00000,0b00000,0b00000]))
        time.sleep(0.1)
        for i in range(5):
            codebug.draw_sprite(0, 0, build_sprite([0b00000,0b00000,0b00000,0b00000,0b10000 >> i]))
            time.sleep(0.1)
        for i in range(5):
            codebug.draw_sprite(0, 0, build_sprite([0b00000,0b00000,0b00000,0b10000 >> i,0b00000]))
            time.sleep(0.1)
        for i in range(5):
            codebug.draw_sprite(0, 0, build_sprite([0b00000,0b00000,0b10000 >> i,0b00000,0b00000]))
            time.sleep(0.1)
        for i in range(5):
            codebug.draw_sprite(0, 0, build_sprite([0b00000,0b10000 >> i,0b00000,0b00000,0b00000]))
            time.sleep(0.1)
        for i in range(5):
            codebug.draw_sprite(0, 0, build_sprite([0b10000 >> i,0b00000,0b00000,0b00000,0b00000]))
            time.sleep(0.1)
