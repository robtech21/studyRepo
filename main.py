#!/usr/bin/env python3

# NOTE: code is currently untested, so I'm not sure if it'll work or not

# Will probably replace 'os' with subprocess soon

import os,termcolor,sys
from termcolor import colored as color
from os import system

inpt = input
pnt  = print

# Definition that allows for the screen to be cleared
def clr():
  system('clear')
  
# Start of the main loop
# This isn't finished and I'll have something that parses arguments that you can run through the script soon
while True:
  clr()
  choice = pnt('''CLI File search utility
Made by the Coding Club
2021
''')
  pnt('File search argument:',str(sys.argv))
