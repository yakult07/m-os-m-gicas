import pyautogui
import my_keyboard 
from time import sleep
from pynput.keyboard import Listener
from pynput import keyboard
from HendlerPoke import HandlerPoke

from utils import get_loot, move_and_click

PLAYER_POSITION = (960, 530)
BP_LOOT_POSITION = (1701,631)
LOOT_POSITION_X =(1900,591)
loot_posição = [(960, 530),(1038,527),(1037,603),(963,599),(885,599),(885,523),(885,446),(961,447)]

list_poke = [(29,702),(31,756),(30,814),(30,864),(32,920),(28,978)]
LIST_ATTACK = ['F1','F2','F3','F4','F5','F6']
list_heal = ['F8']
targe_cor = (232,192,94)
targe_cor_v = (255,0,0)
targe_size = (219,39)

BATTLE_POSITION = (1763,165)
position_battle_x = 1763
position_battle_y = 165

handler_poke = HandlerPoke()

auto_cast = True    

def key_code(key):
    global auto_cast
    # stop
    if key == keyboard.Key.esc:
        return False
    
    # target e full atack
    if key == keyboard.Key.space:
        move_and_click(BATTLE_POSITION, 'left')
        for attack in LIST_ATTACK:
            pyautogui.press(attack)
            pyautogui.moveTo(960, 530)
        pyautogui.press('f10') 

    # troca de poke,target,atack, heal player
    if hasattr(key, 'char') and key.char == 'e': 
        
        handler_poke.next()
        move_and_click(BATTLE_POSITION, 'left')
        sleep(1)
        pyautogui.press(LIST_ATTACK) 
        pyautogui.press(LIST_ATTACK)   
        pyautogui.press('F8')
        move_and_click(BATTLE_POSITION, 'left')
        pyautogui.moveTo(960, 530)

    #troca poke,atack
    if hasattr(key, 'char') and key.char == 'q': 
        handler_poke.previous()
        sleep(1)
        pyautogui.press(LIST_ATTACK) 
        pyautogui.press(LIST_ATTACK)  
        sleep(1)
        pyautogui.moveTo(960, 530)
        
    #loot 1 lugar
    if hasattr(key, 'char') and key.char == '2':
        get_loot(PLAYER_POSITION, BP_LOOT_POSITION,PLAYER_POSITION)
        
    #loot 9 lugar 
    if hasattr(key, 'char') and key.char == '5': 
       if key == keyboard.Key.esc:
            return False
                 
       for i in loot_posição:
            sleep(0)
            move_and_click(i, 'Right')
            move_and_click(BP_LOOT_POSITION, 'Right', 4)
            move_and_click(i,'Right')


    # call poke heal 
    if hasattr(key, 'char') and key.char == '3': 
        
        handler_poke.headling()
        #sleep(1)
        pyautogui.press(LIST_ATTACK) 
        pyautogui.press(LIST_ATTACK)   
        pyautogui.moveTo(960, 530)
        
    # call poke em sequencia e atk 
    if hasattr(key, 'char') and key.char == '4': 
        if auto_cast :
            for call in list_poke:
                auto_cast = True     
                move_and_click(call, 'right')
                sleep(2)
                pyautogui.press(LIST_ATTACK) 
                pyautogui.press(LIST_ATTACK)   
                pyautogui.moveTo(960, 530)
            
        else:
            for call in list_poke:
                auto_cast = False

    if hasattr(key, 'char') and key.char == '1':
        if auto_cast:
            for attack in LIST_ATTACK:
                pyautogui.keyDown(attack)
            auto_cast = False    
        else:
            for attack in LIST_ATTACK:
                pyautogui.keyUp(attack)
            auto_cast = True

    if hasattr(key, 'char') and key.char == '6':
        if auto_cast:
            for heal in list_heal:
                pyautogui.keyDown(heal)
            auto_cast = False    
        else:
            for heal in list_heal:
                pyautogui.keyUp(heal)
            auto_cast = True

         
        
       
     
with Listener(on_release=key_code) as f:
    f.join()