import platform
import argparse
import termios
import tty
import sys
import os

from src.utils.style_output import *

def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Create a project structure.',
        usage='%(prog)s -n [project_name]'
    )

    parser.add_argument('-n', '--project_name', type=str, help='The name of the project directory')

    try:
        return parser.parse_args()
    
    except SystemExit:
        clear_screen()
        print_welcome_message()
        sys.exit(1)

def clear_screen():
    if platform.system() == 'Linux':
        os.system('clear')
    else:
        os.system('cls')

old_settings = None

def disable_input():
    global old_settings
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd) 
    tty.setraw(fd)

def enable_input():
    global old_settings
    if old_settings is not None: 
        fd = sys.stdin.fileno()
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        old_settings = None