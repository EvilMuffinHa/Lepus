class clear:
    def __init__(self, pad):
        self.pad = pad
    #This is an example of how to use the pad. run() uses the pad and clears it
    def run(self):
        #Clearing the pad
        self.pad.clear()
        #Adding the top text and the original text that said "$ clear" beforehand
        with open('config.txt') as f:
            text = ''
            t = f.read()
            for i in t.split('\n\n')[1].split('\n')[1:]:
                text += i
                text += '\n'
            text += t.split('\n\n')[0].split('\n')[-1] + ' clear\n'
        #Adding the command onto the pad after it is cleared
        self.pad.addstr(text)
        #Returning "Done" to show that this command is valid
        return 'Done'