import pyautogui
from time import sleep


def move_and_click(position, side_button,click=1):
    pyautogui.moveTo(position)
    pyautogui.click(button=side_button, clicks=click)


def get_loot(player_position,bp_position,loot_position_x):
    move_and_click(player_position, 'right')
    sleep(1)
    move_and_click(bp_position, 'right', 5)
    sleep(1)
    move_and_click(loot_position_x, 'right',)
