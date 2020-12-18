from .Env import Env


class Checker:
    def __init__(self):
        self.env = Env()

    def reminder(self, file):
        time = self.env.getTime()
        if time >= 17:
            self.env.playWavFile(file)
            self.env.wavWasPlayed()
        else:
            self.env.resetWav()
