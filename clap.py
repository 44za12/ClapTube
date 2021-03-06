#!/usr/bin/python3

from piclap import *
import os

class Config(Settings):
    '''Describes custom configurations and action methods to be executed based
    on the number of claps detected.
    '''

    def __init__(self):
        super().__init__()
        self.chunk_size = 512       # Reduce as power of 2 if pyaudio overflow
        self.interval = 0.5         # Adjust interval between claps
        self.method.value = 9000   # Threshold value adjustment

    def on1Claps(self):
        os.system("open /Applications/Safari.app https://www.youtube.com/watch?v=HhoATZ1Imtw")

    def on2Claps(self):
        '''Custom action for 2 claps'''
        print("You are clapping do something fun?")

    def on3Claps(self):
        '''Custom action for 3 claps'''
        print("Light toggled on pin 6")

    def on100Claps(self):
        print("YOU'RE WEIRD!")


def main():
    config = Config()
    listener = Listener(config)
    listener.start()


if __name__ == '__main__':
    main()
