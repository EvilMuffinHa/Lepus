import os
from inspect import signature

class cmds:
    def __init__(self, pad):
        self.pad = pad
    def run(self):
        text = ''
        #Opening the plugins folder
        dirname = os.path.dirname(__file__)
        #Looking through all the plugins
        for filename in os.listdir(dirname):
            if filename[-3:] == '.py':
                #Checking if it has arguments
                if str(signature(getattr(__import__('plugins.'+filename[0:-3], fromlist=[filename[0:-3]]), filename[0:-3])(self.pad).run)) != '()':
                    #If it has arguments, get the arguments and add it to text
                    text += filename[0:-3] + (' (Args: ' + str(signature(getattr(__import__('plugins.'+filename[0:-3], fromlist=[filename[0:-3]]), filename[0:-3])(self.pad).run)).lstrip('('))
                    text += '\n'
                else:
                    #If it doesn't have arguments, just take the text
                    text += filename[0:-3]
                    text += '\n'
        return text