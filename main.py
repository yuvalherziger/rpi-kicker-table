import json
import RPi.GPIO as GPIO
import time
from pprint import pprint

# load physical I/O configurations:
with open("/home/pi/kicker-goal-detector/config.json") as config_file:
    physical_config = json.load(config_file)

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
    global team_a_score
    global team_b_score
    team_a_score = 0
    team_b_score = 0
    print("Resetting the match")
    print("Current score: Team A - 0:0 - Team B")
    time.sleep(0.4)

def do_cancel_last_increment():
    global team_a_score
    global team_b_score
    if last_increment == "LEFT":
        team_a_score -= 1
    if last_increment == "RIGHT":
        team_b_score -= 1
    print("Current score: Left - " + `left_score` + ":" + `right_score` + " - Right")
    time.sleep(1)

def do_increment_goal(team):
    print(team)

def end_match:
    print("ending match")

GPIO.setmode(GPIO.BCM)
GPIO.setup(reset_match_button_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(cancel_last_increment_button_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

while True:    
    reset_match             = GPIO.input(physical_config["buttons"]["resetMatch"]["inputPin"])
    submit_match            = GPIO.input(physical_config["buttons"]["submitMatch"]["inputPin"])
    sugmit_game             = GPIO.input(physical_config["buttons"]["submitGame"]["inputPin"])
    cancel_last_move        = GPIO.input(physical_config["buttons"]["cancelLastMove"]["inputPin"])
    increment_right_goal    = GPIO.input(physical_config["buttons"]["incrementRightGoal"]["inputPin"])
    increment_left_goal     = GPIO.input(physical_config["buttons"]["incrementLeftGoal"]["inputPin"])
    goal_from_left          = GPIO.input(physical_config["motionSensors"]["rightGoal"]["inputPin"])
    goal_from_right         = GPIO.input(physical_config["motionSensors"]["leftGoal"]["inputPin"])

    # listen to the sensors:
    if goal_from_right == 1:
        do_increment_goal("RIGHT")
    if goal_from_left == 1:
        do_increment_goal("LEFT")

    
    if cancel_last_increment == False:
        do_cancel_last_increment()
        
    if reset_match == False:
        do_reset_match()
    
    

