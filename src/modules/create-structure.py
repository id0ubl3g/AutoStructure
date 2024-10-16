from time import sleep
import sys
import venv
import os
from src.utils.system_utils import *
from src.utils.style_output import *
from docs.structures import *

class CreateStructure:
    def __init__(self):
        self.root_directory: str = "projects"
        self.subdirectories: dict = {}
        self.directory_not_exists: bool = None

    def get_current_directory(self):
        return os.getcwd()
    
    def concatenate_paths(self, project_name):
        current_directory = self.get_current_directory()
        return os.path.join(current_directory, self.root_directory, project_name)
        
    def check_directory_exists(self, project_name):
        self.new_directory_path = self.concatenate_paths(project_name)
        self.directory_not_exists = not os.path.exists(self.new_directory_path)
        return self.directory_not_exists
    
    def create_root_directory(self):
        if self.directory_not_exists:
            sleep(0.8)
            os.makedirs(self.new_directory_path, exist_ok=True)
            print_create_root_directory(self.new_directory_path)
        
        else:
            sleep(0.8)
            print_directory_exists(self.new_directory_path)
            sys.exit(1)
            
    def choice_structure(self):
        while True:
            try:
                choice_structure = input(F'{CYAN}\n[$] {RESET}')
                
                if choice_structure.strip():
                    choice_structure = int(choice_structure)
                    return choice_structure
                
                
                else:
                    sleep(0.8)
                    clear_screen()
                    print_welcome_message()
                    print_invalid_value(choice_structure)

            except KeyboardInterrupt:
                    sleep(0.8)
                    clear_screen()
                    print_welcome_message()
                    print_interrupted_message()
                    sys.exit(1)

            except Exception:
                        sleep(0.8)
                        clear_screen()
                        print_welcome_message()
                        print_invalid_value(choice_structure)

    def pull_structure(self):
        choice_structure = self.choice_structure()
        match choice_structure:
            case 1:
                sleep(0.8)
                self.subdirectories = STRUCTURE_ONE
                clear_screen()
                print_welcome_message()
            
            case _:
                sleep(0.8)
                clear_screen()
                print_welcome_message()
                print_invalid_value(choice_structure)
                self.pull_structure()
            
    def create_subdirectories(self):
        try:
            for subdirectory, subsubdirs in self.subdirectories.items():
                sleep(0.8)
                subdirectory_path = os.path.join(self.new_directory_path, subdirectory)
                os.makedirs(subdirectory_path, exist_ok=True)
                print_create_subdirectory(subdirectory)
            
                for subsubdir in subsubdirs:
                    sleep(0.8)
                    subsubdirectory_path = os.path.join(subdirectory_path, subsubdir)
                    os.makedirs(subsubdirectory_path, exist_ok=True)
                    print_create_subdirectory(subsubdir)
        
        except KeyboardInterrupt:
            sleep(0.8)
            print_interrupted_message()
            sys.exit(1)
        
        except Exception:
            sleep(0.8)
            print_error_unexpected()
            
    def create_virtualenv(self):
        try:
            virtualenv_path = os.path.join(self.new_directory_path, '.venv')
            if not os.path.exists(virtualenv_path):          
                sleep(0.8)
                venv.create(virtualenv_path, with_pip=True)
                print_create_environment(virtualenv_path)

            else:
                sleep(0.8)
                print_environment_exists(virtualenv_path)
        
        except KeyboardInterrupt:
                sleep(0.8)
                print_interrupted_message()
                sys.exit(1)

        except Exception:
            sleep(0.8)
            print_error_unexpected()
    
    def execute(self):
        try:
            args = parse_arguments()
            if not args.project_name:
                clear_screen()
                print_welcome_message()
                sys.exit(1)

            self.project_name = args.project_name
            clear_screen()
            print_welcome_message()
            self.check_directory_exists(self.project_name)
            self.create_root_directory()
            self.pull_structure()
            self.create_subdirectories()
            self.create_virtualenv()
        
        except KeyboardInterrupt:
            sleep(0.8)
            print_interrupted_message()
            sys.exit(1)

        except Exception:
            sleep(0.8)
            print_error_unexpected()
            sys.exit(1)

CreateStructure().execute()
