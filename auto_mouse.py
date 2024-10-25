"""
Filename: auto_mouse.py
Description: Utility to automatically move the mouse cursor.
Author: Gustavo Alves
Date: 2024-10-25
Version: 1.0
"""
import pyautogui as pgi
import keyboard as k
import time, random, os

def auto_mouse():
    position = (random.randint(500,780), random.randint(500,800))
    time_to_move = random.randint(0,2) + 0.5    
    pgi.moveTo(position[0], position[1], time_to_move)
    return position

def end_tool(e):
    print('Good luck at work! =)')
    os._exit(1)

def show_welcome():
    print("""Automatic Mouse Movement Utility
Author: Gustavo Alves
Site: https://github.com/guztavoalves

Instructions:
Press 'ESC' to exit
""",sep='\n')
    
def show_position(pos):
    print(f'Mouse position: x {pos[0]}, y {pos[1]}',end='\r')

def main():

    show_welcome()
    k.on_press_key('esc', end_tool)

    while True:

        for _ in range(random.randint(1,3)):
            show_position(auto_mouse())

        time.sleep(random.randint(1,3)*2)

if __name__ == '__main__':
    main()