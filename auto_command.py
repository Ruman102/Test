import os
import time
import signal
import sys

# Global variable to handle termination
terminate_process = False

def signal_handler(sig, frame):
    global terminate_process
    print("\nProcess Stopped by User (Ctrl+C)")
    terminate_process = True
    sys.exit(0)

# Attach signal handler for Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')  # Windows: cls, Others: clear

def display_header():
    clear_terminal()
    print("=" * 50)
    print(" " * 10 + "Shakhawat Hossain Mozumdar")
    print(" " * 10 + "Contact: https://t.me/techmicroofficial")
    print("=" * 50)

def execute_command(command, interval, repeat_count):
    global terminate_process
    for _ in range(repeat_count):
        if terminate_process:
            break
        os.system(command)
        time.sleep(interval * 60)  # Convert minutes to seconds
    print("\nAll repetitions completed.")

def main():
    display_header()
    while True:
        print("\nEnter the command to execute:")
        command = input("> ")
        
        print("\nEnter the interval (in minutes): ", end="")
        interval = int(input())
        
        print("\nEnter the number of repetitions: ", end="")
        repeat_count = int(input())
        
        print("\nExecuting command...")
        execute_command(command, interval, repeat_count)
        
        print("\nDo you want to execute another command? (y/n): ", end="")
        choice = input().lower()
        if choice != 'y':
            break
    
    print("\nExiting program. Goodbye!")

if __name__ == "__main__":
    main()
    
