import pygame
import time


class SampleProject:
    # T = 2.0/3.0
    # none = 0
    # whole = 4
    # half = 2
    # quarter = 1
    # eight = .5
    # eightT = T * eight
    # sixteen = .25
    # sixteenT = T * sixteen
    # thirtyTwo = .125
    # thirtyTwoT = thirtyTwo * T

    def __init__(self, bpm):
        self.bpm = bpm
        self.noteLength = (1.0 / (4 * 60)) * bpm
        self.stepLength = 64
        self.sampleArray = [-1] * 64

    def addsample(self, sampleNumber, index):
        self.sampleArray[index] = sampleNumber
        # self.quant = 1
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


pygame.mixer.init()
soundb = pygame.mixer.Sound('C:\\Users\\Donald Shoaf\\Desktop\\SAMPLER\\TEST_AUDIO_PCM.wav')
sounda = pygame.mixer.Sound('C:\\Users\\Donald Shoaf\\Desktop\\SAMPLER\\BASS_AUDIO.wav')
masterArray = [sounda, soundb]
channel1 = pygame.mixer.Channel(1)
channel2 = pygame.mixer.Channel(2)
channelArray = [channel1, channel2]

project = SampleProject(60)
project.addsample(0, 0)
project.addsample(1, 4)
project.addsample(1, 8)
print(project.noteLength)
for sampleNumber in project.sampleArray:
    if sampleNumber != -1:
        channelArray[sampleNumber].play(masterArray[sampleNumber])
    time.sleep(project.noteLength)

# channel1.play(soundb)
# sounda.play()

# channel1.play(soundb)
# time.sleep(5)
