import os

class listdir:
    def __init__(self, pad):
        self.pad = pad
    def run(self):
        x = os.listdir('testdir')
        text = ''
        for i in x:
            text += i
            text += '\n'
        return text