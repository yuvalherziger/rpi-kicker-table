import json
import RPi.GPIO as GPIO
import time
from pprint import pprint

# load physical I/O configurations:
with open("../config/config.json") as config_file:
    physical_config = json.load(config_file)

GPIO.setmode(GPIO.BCM)
for button in physical_config["buttons"]:
    GPIO.setup(button["inputPin"], GPIO.IN, pull_up_down = GPIO.PUD_UP)

for motion_sensor in physical_config["motionSensors"]:
    GPIO.setup(motion_sensor["inputPin"], GPIO.IN)

for goal in physical_config["display"]:
    GPIO.setup(goal["outputPin"], GPIO.OUT)

vector_by_digit = {
        ' ': (0, 0, 0, 0, 0, 0, 0),
        '0': (1, 1, 1, 1, 1, 1, 0),
        '1': (0, 1, 1, 0, 0, 0, 0),
        '2': (1, 1, 0, 1, 1, 0, 1),
        '3': (1, 1, 1, 1, 0, 0, 1),
        '4': (0, 1, 1, 0, 0, 1, 1),
        '5': (1, 0, 1, 1, 0, 1, 1),
        '6': (1, 0, 1, 1, 1, 1, 1),
        '7': (1, 1, 1, 0, 0, 0, 0),
        '8': (1, 1, 1, 1, 1, 1, 1),
        '9': (1, 1, 1, 1, 0, 1, 1)
    }

# initialize global match tracking:
left_score = 0
right_score = 0
last_increment = ""

def do_reset_match():
    global right_score
    global left_score
    right_score = 0
    left_score = 0
    print("Resetting the match")
    print("Current score: Left - 0:0 - Right")
    do_update_display()
    time.sleep(0.4)

def do_cancel_last_increment():
    global right_score
    global left_score
    if last_increment == "RIGHT":
        right_score = right_score + 1 if right_score > 0 else 0
    if last_increment == "LEFT":
        left_score = left_score + 1 if left_score > 0 else 0
    print("Current score: Left - " + `left_score` + ":" + `right_score` + " - Right")
    do_update_display()
    time.sleep(1)

def do_increment_goal(team):
    global right_score
    global left_score
    global last_increment
    if team == "RIGHT":
        right_score += 1
    if team == "LEFT":
        left_score += 1
    last_increment = team
    do_update_display()

# TODO implement
def do_end_match:
    print("ending match")

def do_update_display():
    global right_score
    global left_score
    global vector_by_digit
    GPIO.output(physical_config["display"]["rightGoal"]["outputPin"], vector_by_digit(str(right_score)))
    GPIO.output(physical_config["display"]["leftGoal"]["outputPin"], vector_by_digit(str(left_score)))

while True:
    # get all buttons' state
    reset_match             = GPIO.input(physical_config["buttons"]["resetMatch"]["inputPin"])
    submit_match            = GPIO.input(physical_config["buttons"]["submitMatch"]["inputPin"])
    sugmit_game             = GPIO.input(physical_config["buttons"]["submitGame"]["inputPin"])
    cancel_last_move        = GPIO.input(physical_config["buttons"]["cancelLastMove"]["inputPin"])
    increment_right_goal    = GPIO.input(physical_config["buttons"]["incrementRightGoal"]["inputPin"])
    increment_left_goal     = GPIO.input(physical_config["buttons"]["incrementLeftGoal"]["inputPin"])
    # get all sensors' state
    goal_from_left          = GPIO.input(physical_config["motionSensors"]["rightGoal"]["inputPin"])
    goal_from_right         = GPIO.input(physical_config["motionSensors"]["leftGoal"]["inputPin"])

    # listen to sensors:
    if goal_from_right == 1:
        do_increment_goal("RIGHT")
    if goal_from_left == 1:
        do_increment_goal("LEFT")

    # listen to buttons:
    if cancel_last_increment == False:
        do_cancel_last_increment()

    if reset_match == False:
        do_reset_match()
