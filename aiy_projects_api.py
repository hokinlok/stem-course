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

################################################################################
# Write your code inside this region
#



#
# Do not edit anything outside this region
################################################################################
