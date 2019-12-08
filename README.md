# Lepus

![Lepus Logo](/lepus.png)


A framework for building consoles in python.


Lepus is very easy to use. Just write plugins into the plugins folder to create commands on the console. Some examples have been given there.

## Creating Plugins

1. Name a python file with the command you would like.
2. Create a class with the name of the plugin.
3. Initialize the class with the variable "pad". This allows you to access and use the curses.pad object from your plugin, as seen in clear.py
4. Write a function run() within your class, and have it return what you would like. Add parameters to run to add arguments to your command.

Some example plugins are in the plugins folder. Do not use "quit" or "exit" as plugin names.

## Configurations

In config.txt, you can change configurations for the console.
* Beginning Command Text: The text before every command. This can be changed in the middle of a run. For example, `$ cd test` changes the beginning text to `test$ ` in bash.
* Top Text: The text at the top when starting the console.
* Loggging Style: Allows you to change whether the logging accumulates, or rewrites. Change logging style to "Append" to store previous sessions on your console, or keep it as "Rewrite" to rewrite over previous sessions.
* Incorrect Usage: Text that is displayed when a command is used incorrectly.
* Unknown Command: Text that is displayed when a command is unknown.
* Backspace Beep: Whether the computer will beep if it cannot backspace on the console.
* Y Size: Height of the console. 10 is recommended as the minimum.
* X Size: Width of the console. 20 is recommended as the minimum.

## Running

Run `python lepus.py` to produce the console.

## Prerequisites

All you need is python 3.6.
