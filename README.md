# Lepus
A framework for building consoles in python


Lepus is very easy to use. Just write plugins into the plugins folder to create commands on the console. Some examples have been given there.

## Creating Plugins

1. Name a python file with the command you would like.
2. Create a class with the name of the plugin.
3. Initialize the class with the variable "pad". This allows you to access and use the curses.pad object from your plugin, as seen in clear.py
4. Write a function run() within your class, and have it return what you would like. Add parameters to run to add arguments to your command.
