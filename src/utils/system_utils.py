import platform
import argparse
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