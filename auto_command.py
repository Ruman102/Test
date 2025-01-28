
import os
import time
import keyboard

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')  # Windows: cls, Others: clear

def display_header():
    clear_terminal()
    print("=" * 50)
    print(" " * 10 + "Shakhawat Hossain Mozumdar")
    print(" " * 10 + "Contact: https://t.me/techmicroofficial")
    print("=" * 50)

def execute_command(command, interval, repeat_count):
    for _ in range(repeat_count):
        os.system(command)
        time.sleep(interval * 60)  # Convert minutes to seconds
        if keyboard.is_pressed("ctrl+x"):  # Stop with Ctrl+X
            print("\nProcess Stopped by User (Ctrl+X)")
            return
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
