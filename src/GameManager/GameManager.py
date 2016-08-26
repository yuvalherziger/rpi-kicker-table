import json
import RPi.GPIO as GPIO
import time
from pprint import pprint

class GameManager:

    # config:
    physical_config = None
    # game states:
    right_score = 0
    left_score = 0
    last_increment = ""
    # buttons state:
    reset_match = None
    submit_match = None
    sugmit_game = None
    cancel_last_move = None
    increment_right_goal = None
    increment_left_goal = None
    # sensors state:
    goal_from_left = None
    goal_from_right = None

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

    def __init__(self):
        # load physical I/O configurations:
        with open("../config/config.json") as config_file:
            self.physical_config = json.load(config_file)

        GPIO.setmode(GPIO.BCM)
        for button in physical_config["buttons"]:
            GPIO.setup(button["inputPin"], GPIO.IN, pull_up_down = GPIO.PUD_UP)

        for motion_sensor in physical_config["motionSensors"]:
            GPIO.setup(motion_sensor["inputPin"], GPIO.IN)

        for goal in physical_config["display"]:
            GPIO.setup(goal["outputPin"], GPIO.OUT)

    def run(self):
        while True:
            # get all buttons' state
            self.__getPhysicalStates()

            # listen to sensors:
            if goal_from_right == 1:
                self.__incrementGoal("RIGHT")
            if goal_from_left == 1:
                self.__incrementGoal("LEFT")

            # listen to buttons:
            if cancel_last_increment == False:
                self.__cancelLastIncrement()

            if reset_match == False:
                self.__resetMatch()

    def __getPhysicalStates:
        self.reset_match             = GPIO.input(self.physical_config["buttons"]["resetMatch"]["inputPin"])
        self.submit_match            = GPIO.input(self.physical_config["buttons"]["submitMatch"]["inputPin"])
        self.sugmit_game             = GPIO.input(self.physical_config["buttons"]["submitGame"]["inputPin"])
        self.cancel_last_move        = GPIO.input(self.physical_config["buttons"]["cancelLastMove"]["inputPin"])
        self.increment_right_goal    = GPIO.input(self.physical_config["buttons"]["incrementRightGoal"]["inputPin"])
        self.increment_left_goal     = GPIO.input(self.physical_config["buttons"]["incrementLeftGoal"]["inputPin"])
        # get all sensors' state
        self.goal_from_left          = GPIO.input(self.physical_config["motionSensors"]["rightGoal"]["inputPin"])
        self.goal_from_right         = GPIO.input(self.physical_config["motionSensors"]["leftGoal"]["inputPin"])

    def __resetMatch(self):
        self.right_score = 0
        self.left_score = 0
        print("Resetting the match")
        print("Current score: Left - 0:0 - Right")
        self.__updateDisplay()
        time.sleep(0.4)

    def __cancelLastIncrement(self):
        if self.last_increment == "RIGHT":
            self.right_score = self.right_score + 1 if self.right_score > 0 else 0
        if self.last_increment == "LEFT":
            self.left_score = self.left_score + 1 if self.left_score > 0 else 0
        print("Current score: Left - " + `self.left_score` + ":" + `self.right_score` + " - Right")
        self.__updateDisplay()
        time.sleep(1)

    def __incrementGoal(team):
        if team == "RIGHT":
            self.right_score += 1
        if team == "LEFT":
            self.left_score += 1
        self.last_increment = team
        self.__updateDisplay()

    # TODO implement
    def __endMatch:
        print("ending match")

    def __updateDisplay(self):
        GPIO.output(self.physical_config["display"]["rightGoal"]["outputPin"], self.vector_by_digit(str(self.right_score)))
        GPIO.output(self.physical_config["display"]["leftGoal"]["outputPin"], self.vector_by_digit(str(self.left_score)))
