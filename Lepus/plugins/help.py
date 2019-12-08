class help:
    def __init__(self, pad):
        self.pad = pad
    def run(self):
        return '''Write plugins for the console by
making a .py file named with the name of the plugin
and add a class named with the name of the plugin
and adding an __init__(self, pad) so that if you want,
your plugin can edit the actual curses pad. 
Then, return what you want to say in a 
function called "run" in that class.
If text doesn't fit, maybe make it two pages, or 
use config.txt and change the size of the pad.
This is an example of how to return a long 
block of text.'''