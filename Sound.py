import pygame
import time


class SampleProject:
    T = 2.0/3.0
    none = 0
    whole = 4
    half = 2
    quarter = 1
    eight = .5
    eightT = T * eight
    sixteen = .25
    sixteenT = T * sixteen
    thirtyTwo = .125
    thirtyTwoT = thirtyTwo * T

    def __init__(self, bpm):
        self.bpm = bpm
        self.stepLength = 64
        self.quant = 1
        # 0 = no quantization TODO
        # 1 = whole
        # 2 = half
        # 3 = quarter
        # 4 = eighth
        # 43 = eighth triplet
        # 5 = sixteenth
        # 53 = sixteenth triplet
        # 6 = thirty second
        # 63 = thirty second triplet


sound = Sound('C:\\Users\\Donald Shoaf\\Desktop\\SAMPLER\\TEST_AUDIO_PCM.wav')
# pygame.init()
pygame.mixer.init()
soundb = pygame.mixer.Sound('C:\\Users\\Donald Shoaf\\Desktop\\SAMPLER\\TEST_AUDIO_PCM.wav')
sounda = pygame.mixer.Sound('C:\\Users\\Donald Shoaf\\Desktop\\SAMPLER\\BASS_AUDIO.wav')
channel1 = pygame.mixer.Channel(1)
channel1.play(soundb)
sounda.play()
while channel1.get_busy():
    a = 0
channel1.play(soundb)
time.sleep(5)
