class view:
    def __init__(self, pad):
        self.pad = pad
    def run(self, filename):
        try:
            path = 'testdir/' + filename + '.txt'
            with open(path, 'r') as f:
                text =f.read()
            return text
        except:
            return "File not found."