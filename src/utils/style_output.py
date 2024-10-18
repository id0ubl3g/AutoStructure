RESET = "\033[0m"
BOLD = "\033[1m"
WHITE = "\033[37m"
BLUE = "\033[34m"
YELLOW = "\033[33m"
RED = '\033[91m'
CYAN = '\033[96m'
ORANGE = "\033[38;5;208m"

def print_welcome_message():
    print(rf'''{CYAN}

    _         _          ____  _                   _                  
   / \  _   _| |_ ___   / ___|| |_ _ __ _   _  ___| |_ _   _ _ __ ___ 
  / _ \| | | | __/ _ \  \___ \| __| '__| | | |/ __| __| | | | '__/ _ \
 / ___ \ |_| | || (_) |  ___) | |_| |  | |_| | (__| |_| |_| | | |  __/
/_/   \_\__,_|\__\___/  |____/ \__|_|   \__,_|\___|\__|\__,_|_|  \___|
            {RESET}{WHITE}Flexible Python project structures for every need.
            {RESET}{CYAN}
        [*]__author__: @id0ubl3g
        [*]__version__: 1.0 
        [*]__usage__: {YELLOW}python3{RESET} main.py -n {CYAN}[project_name]{RESET}
''')

def print_create_root_directory(directory_name):
    print(f'\n{CYAN}[+]{RESET} Creating root directory at: {WHITE}{directory_name}{RESET}')

def print_directory_exists(directory_name): #ALTERNATIVE
    print(f'{CYAN}[i]{RESET} Directory already exists: {WHITE}{directory_name}{RESET}')

def print_create_subdirectory(subdirectory):
    print(f'\n{CYAN}[+]{RESET} Creating subdirectory: {WHITE}{subdirectory}{RESET}')

def print_create_environment(virtualenv_path):
    print(f'\n{CYAN}[+]{RESET} Virtual environment created at: {WHITE}{virtualenv_path}{RESET}')

def print_environment_exists(virtualenv_path):
    print(f'\n{ORANGE}[i]{RESET} Virtual environment already exists at: {WHITE}{virtualenv_path}{RESET}')

def print_environment_error(virtualenv_path):
    print(f'\n{RED}[x]{RESET} Failed to create virtual environment at: {WHITE}{virtualenv_path}{RESET}')

def print_interrupted_message():
    print(f'\n{ORANGE}[!]{RESET} Operation interrupted by user. Exiting gracefully...')

def print_structure_created(directory_name):
    print(f'\n{CYAN}[+]{RESET} Project structure created successfully at: {WHITE}{directory_name}{RESET}')

def print_structure_exists(directory_name): #ALTERNATIVE
    print(f'\n{ORANGE}[i]{RESET} Project structure already exists at: {WHITE}{directory_name}{RESET}')

def print_invalid_value(message):  # Função para imprimir mensagem de valor inválido
    print(f'\n{ORANGE}[i]{RESET} Invalid value: {WHITE}{message}{RESET}')

def print_error_unexpected():
    print(f'\n{RED}[x]{RESET} An unexpected error occurred.')

def print_project_options():
    print(f'\n{CYAN}[+]{RESET}{BOLD} Select a project structure to set up:{RESET}\n')
    print(f'{CYAN}[1]{RESET} Scalabre Structure: Basic scalable structure{RESET}')
    print(f'{CYAN}[2]{RESET} API Clean Structure: Clean and modular API structure{RESET}')
    print(f'{CYAN}[3]{RESET} Site Structure: Structure for web applications{RESET}')
    
def print_create_file(file_name):
    print(f'\n{CYAN}[+]{RESET} Creating file: {WHITE}{file_name}{RESET}')


def print_license_options():
    print(f'\n{CYAN}[+]{RESET}{BOLD} Select a license for your project:{RESET}\n')
    print(f'{CYAN}[1]{RESET} MIT License{RESET}')
    print(f'{CYAN}[2]{RESET} GNU General Public License{RESET}')
    print(f'{CYAN}[3]{RESET} Apache License 2.0{RESET}')

def print_create_license(license_name):
    print(f'\n{CYAN}[+]{RESET} Creating license: {WHITE}{license_name}{RESET}')