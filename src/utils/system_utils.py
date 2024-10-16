import argparse
import sys

def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Create a project structure.',
        usage='%(prog)s -n [project_name]'
    )

    parser.add_argument('-n', '--project_name', type=str, help='The name of the project directory')

    try:
        return parser.parse_args()
    
    except SystemExit:
        sys.exit(1)