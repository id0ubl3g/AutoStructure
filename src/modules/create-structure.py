import os

class CreateStructure:
    def __init__(self):
        self.root_directory: str = "projects"
        self.subdirectories = []
        self.directory_not_exists: bool = None

    def get_current_directory(self):
        return os.getcwd()
    
    def concatenate_paths(self, project_name):
        current_directory = self.get_current_directory()
        new_directory_path = os.path.join(current_directory, self.root_directory, project_name)
        return new_directory_path

    

