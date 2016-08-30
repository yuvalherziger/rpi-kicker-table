import pygame
import random
class MediaManager:

    def __init__(self):
        pygame.mixer.init()

    def randomPlay(self, paths):
        if len(paths) > 0:
            path = random.choice(paths)
            self.play(path)

    def play(self, path):
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
        
    
