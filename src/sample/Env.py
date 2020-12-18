class Env:
    def __init__(self):
        self.played = False

    def getTime(self):
        pass

    def playWavFile(self, file):
        pass

    def wavWasPlayed(self):
        self.played = True

    def resetWav(self):
        self.played = False
