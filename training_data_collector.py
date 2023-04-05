#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Parameters:
--label: a string specifying the name of the class (label) of the collected images
--num_images: number of images to record during the session    

Example:
training_data_collector.py --label no_hands --num_images 100
"""

import argparse
import time
import os
import random
import string

from aiy.board import Board
from aiy.leds import Color, Leds, Pattern
from aiy.pins import BUZZER_GPIO_PIN
from aiy.toneplayer import TonePlayer
from picamera import PiCamera

# Board (controls the top button)
board = Board()

# Leds (controls the LED in the top button, and the privacy LED)
leds = Leds()

# Tone player (plays music using the piezo buzzer)
toneplayer = TonePlayer(BUZZER_GPIO_PIN)

# Global variables
path_to_training_folder = "training_data/"

# Create training_data folder if it does not exist
if not os.path.exists(path_to_training_folder):
    os.makedirs(path_to_training_folder)

def main():
    """Face detection camera inference example."""
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--label',
        '-lbl',
        type=str,
        dest='label',
        required=True,
        help='Specifies the class (label) of training images (e.g. no_hangs).')

    parser.add_argument(
        '--num_images',
        '-nimg',
        type=int,
        dest='num_images',
        default=10,
        help='Sets the number of training images to make.')

    args = parser.parse_args()

    with PiCamera(sensor_mode=4, resolution=(1640, 1232), framerate=4) as camera:
        # Start the camera stream.
        camera.start_preview()

        label = args.label
        num_images = int(args.num_images)

        output_folder = path_to_training_folder + label.lower() + '/'
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        def capture_image():
            random_string = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))
            img_name = output_folder + label.lower() + '_' + random_string + '.jpg'
            camera.capture(img_name)

        ########################################################################
        # Write your code inside this region
        #
        # 1. Light up the RGB LED with a breathing pattern at the start



        # 2. Wait until the button is pressed



        #
        # Do not edit anything outside this region
        ########################################################################

        # 3. Capture `num_images` training images in total
        #    - Use the `capture_image` function

        for i in range(num_images):
            capture_image()

            ####################################################################
            # Write your code inside this region
            #
            # 4. For each image taken, light up the RGB LED once and play a beep



            #
            # Do not edit anything outside this region
            ####################################################################

            print('Captured', str(i + 1), 'out of', str(num_images))
            time.sleep(1)

        camera.stop_preview()

        ########################################################################
        # Write your code inside this region
        #
        # 5. Play a song when the collection is completed



        #
        # Do not edit anything outside this region
        ########################################################################

if __name__ == '__main__':
    main()
