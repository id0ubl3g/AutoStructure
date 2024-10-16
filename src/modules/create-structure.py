import os
import subprocess
import sys

from docs.structures import *

class CreateStructure:
    def __init__(self):
        self.root_directory: str = "projects"
        self.subdirectories = []
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
            os.makedirs(self.new_directory_path, exist_ok=True)
        
        else:
            pass
    
    def choice_structure(self):
        choice_structure = int(input('$ '))
        return choice_structure
    
    def pull_structure(self):
        choice_structure = self.choice_structure()
        match choice_structure:
            case 1:
                self.subdirectories = STRUCTURE_ONE
            
            case _:
                pass
                
    def create_subdirectories(self):
        for subdirectory, subsubdirs in self.subdirectories.items():
            subdirectory_path = os.path.join(self.new_directory_path, subdirectory)
            os.makedirs(subdirectory_path, exist_ok=True)

            for subsubdir in subsubdirs:
                subsubdirectory_path = os.path.join(subdirectory_path, subsubdir)
                os.makedirs(subsubdirectory_path, exist_ok=True)
    
    def create_virtualenv(self):
        virtualenv_path = os.path.join(self.new_directory_path, '.venv')
        if not os.path.exists(virtualenv_path):
            try:
                subprocess.check_call([sys.executable, '-m', 'venv', virtualenv_path])
            
            except Exception:
                pass

        else:
            pass
        