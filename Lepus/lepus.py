from curses import *
import os
from inspect import signature
screen_size_too_small = 0


def disp(wy, wx, pad_pos, pad, text):
    if getsyx()[0] >= wy - len(text.split('\n')):
        pad_pos += 1
        wy += 1
        pad.resize(wy, wx)
        pad.addstr(text)
    else:
        pad.addstr(text)



def colores(color):
    if color == 'BLACK':
        return COLOR_BLACK
    if color == 'WHITE':
        return COLOR_WHITE
    if color == 'YELLOW':
        return COLOR_YELLOW
    if color == 'CYAN':
        return COLOR_CYAN
    if color == 'BLUE':
        return COLOR_BLUE
    if color == 'RED':
        return COLOR_RED
    if color == 'MAGENTA':
        return COLOR_MAGENTA
    if color == 'GREEN':
        return COLOR_GREEN


def main(stdscr):


    #Initializing variables
    global allcmds, cmds, log, screen_size_too_small
    allcmds = []
    log = []
    pointer = -1

    #Opening config.txt and initializing the configurations
    f = open('config.txt', 'r')
    text = f.read()
    f.close()
    wx = int(text.split('\n\n')[-1].split(' ')[-1])
    wy = int(text.split('\n\n')[-2].split(' ')[-1])
    top_text = ''
    for i in text.split('\n\n')[1].split('\n')[1:]:
        top_text += i
        top_text += '\n'
    start_text = ''
    for i in text.split('\n\n')[0].split('\n')[1:]:
        start_text += i
    backbeep = text.split('\n\n')[-3]
    start_text += ' '
    cmd = ''
    unknown = text.split('\n\n')[-4].split('\n')[-1]
    incorrect = text.split('\n\n')[-5].split('\n')[-1]


    #Initializing plugins
    path = 'plugins/'
    allfiles = os.listdir(path)
    cmds = ['quit', 'exit']
    for i in allfiles:
        if i[-3] == '.':
            cmds.append(i[0:-3])

    #Creating a new pad
    pad = newpad(wy,wx)
    pad_pos = 0
    disp(wy, wx, pad_pos, pad, top_text)
    disp(wy, wx, pad_pos, pad, start_text)
    pad.keypad(True)
    pad.scrollok(1)



    #Running the loop for the console
    while True:

        #Updating the pad
        try:
            pad.refresh(pad_pos, 0, 0, 0, wy, wx)
        except:
            screen_size_too_small = 1
            break

        #Getting Key
        x = pad.getkey()


        #Checking the Arrow Keys: Allows you to click up and down to access previous commands.
        if x == 'KEY_UP':
            try:
                cmd = allcmds[pointer]
                pad.addstr('\b \b' * (getsyx()[1] - len(start_text)) + cmd)
                pointer -= 1
            except IndexError:
                pass
        elif x == 'KEY_DOWN':
            if pointer < -2:
                cmd = allcmds[pointer + 2]
                pad.addstr('\b \b' * (getsyx()[1] - len(start_text)) + cmd)
                pointer += 1
            else:
                cmd = ''
                pad.addstr('\b \b' * (getsyx()[1] - len(start_text)))
                pointer = -1
        elif x == 'KEY_RIGHT':
            pass
        elif x == 'KEY_LEFT':
            pass


        #Esc will break out
        elif ord(x) == 27:
            pad.scrollok(0)
            use_default_colors()
            os.system('stty sane')
            break

        #If you hit enter, it adds the start_text
        elif ord(x) == 10:
            disp(wy, wx, pad_pos, pad, '\n')
            pointer = -1
            #Updating start text in case user decides to change the file based on a plugin
            start_text = ''
            for i in text.split('\n\n')[0].split('\n')[1:]:
                start_text += i
            start_text += ' '
            allcmds.append(cmd)

            comd = cmd.split(' ')[0]

            #Checking if cmd is an actual command
            if comd not in cmds:
                disp(wy, wx, pad_pos, pad, unknown)
                log.append(unknown)
                disp(wy, wx, pad_pos, pad, '\n')
            if (comd in cmds) and (comd != 'quit' and comd != 'exit'):
                #Checking all the arguments, and if they are valid
                sig = signature(getattr(__import__('plugins.' + comd,fromlist=[comd]), comd)(pad).run)
                args = str(sig)
                argslist = []


                #moving around the arguments
                for i in args.split(','):
                    argslist.append(i.rstrip().lstrip().rstrip(')').lstrip('('))

                #If arg-length is correct
                if len(cmd.rstrip().split(' ')) - 1 == len(argslist) or (len(cmd.rstrip().split(' ')) == len(argslist) and argslist == ['']):
                    if argslist == ['']:

                        # importing and running the class, and then running the function run() inside that
                        x = getattr(__import__('plugins.' + comd,fromlist=[comd]), comd)(pad).run()
                        log.append(x)
                        disp(wy, wx, pad_pos, pad, x)
                    else:

                        # importing and running the class, and then running the function run() inside that
                        x = getattr(__import__('plugins.' + comd,fromlist=[comd]), comd)(pad).run(*cmd.rstrip().split(' ')[1:])
                        log.append(x)
                        disp(wy, wx, pad_pos, pad, x)

                else:
                    disp(wy, wx, pad_pos, pad, incorrect)
                    log.append(incorrect)
                disp(wy, wx, pad_pos, pad, '\n')

            if comd == 'quit' or comd == 'exit':
                if len(cmd.rstrip().split(' ')) == 1:
                    break
                else:
                    disp(wy, wx, pad_pos, pad, incorrect)
                    log.append(incorrect)
                    disp(wy, wx, pad_pos, pad, '\n')



            #Adding the next line start text
            disp(wy, wx, pad_pos, pad, start_text)
            #Restarting the command
            cmd = ''


        #Backspace keys
        elif (ord(x) == 8 or ord(x) == 127 or ord(x) == KEY_BACKSPACE or x == '\x7f'):
            pointer = -1
            #Checking whether it is as long as the start_text
            start_text = ''
            for i in text.split('\n\n')[0].split('\n')[1:]:
                start_text += i
            start_text += ' '
            if getsyx()[1] > len(start_text):
                disp(wy, wx, pad_pos, pad, '\b \b')
                cmd = cmd[0:-1]
            #Beep!
            else:
                if backbeep.lower() == 'backspace beep: yes':
                    beep()
                else:
                    pass
        else:
            #Adding the character if it isn't a special key
            disp(wy, wx, pad_pos, pad, x)
            cmd += x


        #If the position is at the bottom of the pad, shift it so it will scroll
        if getsyx()[0] == wy:
            pad_pos += 1
            wy+=1
            pad.resize(wy,wx)

    if text.split('\n\n')[2].lower() == 'logging style: append':
        f = open('log.txt', 'a')
        f.write('\n\n')
        for a, b in zip(allcmds, log):
            f.write(a + ': ' + b + '\n')

    elif text.split('\n\n')[2].lower() == 'logging style: rewrite':
        f = open('log.txt', 'w')
        f.write('\n\n')
        for a, b in zip(allcmds, log):
            f.write(a + ': ' + b + '\n\n')

wrapper(main)

if screen_size_too_small == 1:
    print('Screen size is too small.')
os.system('stty sane')

def end(stdscr):
    stdscr.clear()
wrapper(end)
os.system('cls' if os.name == 'nt' else 'clear')
use_default_colors()
