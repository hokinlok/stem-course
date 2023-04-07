#!/usr/bin/env python3
import time

from aiy.board import Board
from aiy.leds import Color, Leds, Pattern
from aiy.pins import BUZZER_GPIO_PIN
from aiy.toneplayer import TonePlayer

# Board (controls the top button)
board = Board()

# Leds (controls the LED in the top button, and the privacy LED)
leds = Leds()

# Tone player (plays music using the piezo buzzer)
toneplayer = TonePlayer(BUZZER_GPIO_PIN)

leds.update(Leds.rgb_on(Color.RED))
time.sleep(1)
leds.update(Leds.rgb_on(Color.YELLOW))
time.sleep(1)
leds.update(Leds.rgb_on(Color.GREEN))
time.sleep(1)
leds.update(Leds.rgb_on(Color.CYAN))

board.button.wait_for_press()
board.button.wait_for_release()

leds.pattern = Pattern.blink(500)
leds.update(Leds.rgb_pattern(Color.BLUE))

board.button.wait_for_press()
board.button.wait_for_release()

leds.pattern = Pattern.breathe(1000)
leds.update(Leds.rgb_pattern(Color.PURPLE))

board.button.wait_for_press()
board.button.wait_for_release()

leds.update(Leds.rgb_off())

imperial_march = [
  'A3q', 'A3q', 'A3q', 'F3e', 'C4e',
  'A3q', 'F3e', 'C4e', 'A3h',
  'E4q', 'E4q', 'E4q', 'F4e', 'C4e',
  'g3q', 'F3e', 'C4e', 'A3h',
]
toneplayer.play(*imperial_march)
