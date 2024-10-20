from src.utils.style_output import *
from src.utils.system_utils import clear_screen

from time import sleep
import subprocess
import signal
import sys

def handle_sigint(signal_received, frame):
    clear_screen()
    print_welcome_message()
    print_process_interrupted()
    sys.exit(0)

def check_if_root():
    current_user = subprocess.run(
        ["whoami"],
        text=True,
        capture_output=True,
        check=True
    )
    return current_user.stdout.strip() == 'root'

def run_sudo():
    try:
        if check_if_root():
            sleep(2)
            clear_screen()
            print_welcome_message()
            print_already_logged_as_root()
            sleep(2)

            return
        
        sleep(2)
        clear_screen()
        print_welcome_message()
        print_prompt_password_message()
        sleep(2)

        signal.signal(signal.SIGINT, handle_sigint)

        subprocess.run([
            "sudo",
            "su"],
        check=True
        )

        return
    except KeyboardInterrupt:
        clear_screen()
        print_welcome_message()
        print_process_interrupted()
        sys.exit(0)

    except subprocess.CalledProcessError as e:
        if e.returncode == 130:
            clear_screen()
            print_welcome_message()
            print_process_interrupted()
        else:
            clear_screen()
            print_welcome_message()
            print_password_or_error()
            sys.exit(1)

if __name__ == "__main__":
    run_sudo()
