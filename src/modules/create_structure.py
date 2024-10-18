from time import sleep
import venv
import sys
import os

from src.utils.system_utils import *
from src.utils.style_output import *
from config.structures import *
from config.liceses import *

class CreateStructure:
    def __init__(self):
        self.root_directory: str = "projects"
        self.subdirectories: dict = {}
        self.directory_not_exists: bool = None
        self.init_files: list = ['README.md', '.gitignore', '.env', '.env.example', 'LICENSE']

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
            sleep(0.5)
            os.makedirs(self.new_directory_path, exist_ok=True)
            print_create_root_directory(self.new_directory_path)
        
        else:
            sleep(0.5)
            print_directory_exists(self.new_directory_path)
            sys.exit(1)
            
    def choice_structure(self):
        while True:
            try:
                print_project_options()
                choice_structure = input(F'{CYAN}\n[$] {RESET}')
                
                if choice_structure.strip():
                    choice_structure = int(choice_structure)
                    return choice_structure
                
                else:
                    sleep(0.5)
                    clear_screen()
                    print_welcome_message()
                    print_invalid_value(choice_structure)

            except KeyboardInterrupt:
                    sleep(0.5)
                    clear_screen()
                    print_welcome_message()
                    print_interrupted_message()
                    sys.exit(1)

            except Exception:
                        sleep(0.5)
                        clear_screen()
                        print_welcome_message()
                        print_invalid_value(choice_structure)

    def pull_structure(self):
        sleep(2)
        choice_structure = self.choice_structure()
        match choice_structure:
            case 1:
                sleep(0.5)
                self.subdirectories = SCALABLE_STRUCTURE
                clear_screen()
                print_welcome_message()

            case 2:
                sleep(0.5)
                self.subdirectories = API_CLEAN_STRUCTURE
                clear_screen()
                print_welcome_message()

            case 3:
                sleep(0.5)
                self.subdirectories = SITE_STRUCTURE
                clear_screen()
                print_welcome_message()
            
            case _:
                sleep(0.5)
                clear_screen()
                print_welcome_message()
                print_invalid_value(choice_structure)
                self.pull_structure()
            
    def create_subdirectories(self):
        try:
            for subdirectory, subsubdirs in self.subdirectories.items():
                sleep(0.5)
                subdirectory_path = os.path.join(self.new_directory_path, subdirectory)
                os.makedirs(subdirectory_path, exist_ok=True)
                print_create_subdirectory(subdirectory)
            
                for subsubdir in subsubdirs:
                    sleep(0.5)
                    subsubdirectory_path = os.path.join(subdirectory_path, subsubdir)
                    os.makedirs(subsubdirectory_path, exist_ok=True)
                    print_create_subdirectory(subsubdir)
        
        except KeyboardInterrupt:
            sleep(0.5)
            print_interrupted_message()
            sys.exit(1)
        
        except Exception:
            sleep(0.5)
            print_error_unexpected()

    def create_files(self, project_name):
        try:
            sleep(0.5)
            src_schemas_path = os.path.join(self.new_directory_path, 'src', 'schemas')
            app_schemas_path = os.path.join(self.new_directory_path, 'app', 'schemas')

            if os.path.exists(src_schemas_path):
                gitkeep_path = os.path.join(src_schemas_path, '.gitkeep')
                with open(gitkeep_path, 'w') as file:
                    file.write('')

                print_create_file('.gitkeep')

            if os.path.exists(app_schemas_path):
                gitkeep_path = os.path.join(app_schemas_path, '.gitkeep')
                with open(gitkeep_path, 'w') as file:
                    file.write('')
                    
                print_create_file('.gitkeep')


            for file in self.init_files:
                sleep(0.5)

                create_file = os.path.join(self.new_directory_path, file)
                print_create_file(file)
                
                if 'README.md' in create_file:
                    with open(create_file, 'w') as file:
                        file.write(project_name)

                elif '.gitignore' in create_file:
                    with open(create_file, 'w') as file:
                        file.write(f'__pycache__/\n\nvenv/\n.env\nschemas/*')
                
                elif 'LICENSE' in create_file:
                    sleep(2)
                    clear_screen()
                    print_welcome_message()
                    print_license_options()
                    choice_license = input(F'{CYAN}\n[$] {RESET}')
                    match choice_license:
                        case '1':
                            sleep(0.5)
                            with open(create_file, 'w') as file:
                                file.write(MIT)

                            sleep(0.5)  
                            print_create_license('MIT')

                        case '2':
                            sleep(0.5)
                            with open(create_file, 'w') as file:
                                file.write(GNU)
                            
                            sleep(0.5)
                            print_create_license('GNU')

                        case '3':
                            sleep(0.5)
                            with open(create_file, 'w') as file:
                                file.write(APACHE)
                            
                            sleep(0.5)  
                            print_create_license('APACHE')

                        case _:
                            sleep(0.5)
                            clear_screen()
                            print_welcome_message()
                            print_invalid_value(choice_license)
                            self.create_files(project_name)

                else:
                    with open(create_file, 'w') as file:
                        file.write('')
        
        except KeyboardInterrupt:
                sleep(0.5)
                print_interrupted_message()
                sys.exit(1)

        except Exception:
            sleep(0.5)
            print_error_unexpected()
        
    def create_virtualenv(self):
        try:
            virtualenv_path = os.path.join(self.new_directory_path, '.venv')
            if not os.path.exists(virtualenv_path):          
                sleep(0.5)
                venv.create(virtualenv_path, with_pip=True)
                print_create_environment(virtualenv_path)

            else:
                sleep(0.5)
                print_environment_exists(virtualenv_path)
        
        except KeyboardInterrupt:
                sleep(0.5)
                print_interrupted_message()
                sys.exit(1)

        except Exception:
            sleep(0.5)
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
            self.create_files(self.project_name)
            self.create_virtualenv()
        
        except KeyboardInterrupt:
            sleep(0.5)
            print_interrupted_message()
            sys.exit(1)

        except Exception:
            sleep(0.5)
            print_error_unexpected()
            sys.exit(1)