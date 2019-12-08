Lepus is a console framework which allows you to build your own console.

In config.txt, you can change console configurations.

The beginning command text is the text that goes at the beginning of each command.
The beginning command text can be changed in the middle of the run as it gets updated every command.
For example, you can make it like bash, where you can change it with "cd".

The top text is the text at the top of the terminal.

Logging style concerns log.txt. If you want to save past sessions, change Logging Style to "Append".
If you would like it to write over previous sessions, change Logging Style to "Rewrite".

Incorrect Usage is the text that will be displayed if you use the command without adding the right amount of arguments.

Unknown Command displays text if that command is not within plugins.

If Backspace Beep is yes, it will beep if you cannot backspace any more. If it is no, it will not beep.

Y size is the height of the curses.pad object. It dictates how far you can write before the console starts scrolling.
It should be at minimum 10.

X size is the length of the curses.pad object. It dictates how much you can type on one line before scrolling down to the next line.
It should be at minimum 20.

Writing plugins are easy. Name the file what you want the command to be named.
Create a class with the name of the command.
Make sure you have 1 argument when you initialize the class, which is "pad".
This is so that you can use the pad with your own plugins. (See clear.py)
Write a function called run(), which will return what you want to return.
You can have multiple arguments within run, this means that you have multiple arguments to the command withing the console. (See hello.py)
In run(), you must return something. If you don't need to return anything, "Done", or '', is recommended.

Do not use quit or exit as names in your plugins.