import RPi.GPIO as GPIO
import time
import pygame
from GameManager.MediaManager import MediaManager
from pprint import pprint

GPIO.setmode(GPIO.BCM)
# button # 1
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# button # 2
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# button # 3
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# button # 4
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# button # 5
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# button # 6
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)

media_manager = MediaManager()

while True:
    input_1 = GPIO.input(17)
    input_2 = GPIO.input(27)
    input_3 = GPIO.input(22)
    input_4 = GPIO.input(5)
    input_5 = GPIO.input(6)
    input_6 = GPIO.input(13)
    
    if input_1 == False:
        print('1 Pressed')
        media_manager.play("../media/button_1.mp3")
        time.sleep(1)

    if input_2 == False:
        print('2 Pressed')
        media_manager.play("../media/button_2.mp3")
        time.sleep(0.2)

    if input_3 == False:
        print('3 Pressed')
        media_manager.play("../media/button_3.mp3")
        time.sleep(0.2)

    if input_4 == False:
        print('4 Pressed')
        media_manager.play("../media/button_4.mp3")
        time.sleep(0.2)

    if input_5 == False:
        print('5 Pressed')
        media_manager.play("../media/button_5.mp3")
        time.sleep(0.2)

    if input_6 == False:
        print('6 Pressed')
        media_manager.play("../media/button_6.mp3")
        time.sleep(0.2)
    
