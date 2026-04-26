import time
from colorama import Fore, Style, init
import os, sys
os.environ['PYGAME_HIDDEN_SUPPORT_PROMPT'] = '1'
import pygame
import threading

def clear_hide():
    if __name__ == "__main__":
        os.system('cls')
    print("\033[?25l", end="")

clear_hide()

def play_music():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.play(start=84.6)
    while pygame.mixer.music.get_busy():
        time.sleep(1)
        
threading.Thread(target=play_music).start() 

init(convert=True, autoreset=True)

def music_lyric():
    lyrics = [
        (" ", 0, True),
        ("When I'm away from you, I miss your touch", 0.06, True),
        ("You're, the reason I belive in love", 0.055, True,),
        ("I'ts been difficult for me to trust", 0.05, True),
        ("And I'm afraid that I'ma fuck it up", 0.05, True),
        ("", 0, True),
        ("Ain't no way that I can leave you stranded", 0.055, True),
        ("'Cause you ain't ever left me empty-handed", 0.055, True),
        ("And you know that I know that I can't live without you", 0.04, True),
        ("So, baby, stay", 0.06, True),
        (" ", 0, True),
        ("Oh, ooh-whoa", 0.09, True),
        ("Oh, ooh-whoa", 0.08, True),
        ("Oh, ooh-whoa", 0.08, True),
        (" ", 0, True),
        ("I'll be fucked up if you can't be right here", 0.05, True),
        ("I do the same ", 0.05, False),
        ("thing I told you that i never would", 0.04, True),
        ("I told i'd change, ", 0.04, False),
        ("even when I knew I never could", 0.04, True),
        ("I know that I can't ", 0.04, False),
        ("find nobody else as good as you", 0.04, True),
        ("I need you to stay, need you to stay, hey", 0.05, True),
    ]
    return lyrics

delays = [2.5, 0.7, 0.7, 0.8, 0.7, 0.0, 0.8, 0.6, 0.9, 0.7, 0.7, 1.7, 1.7, 1.8, 0.0, 0.6, 0.08, 0.5, 0.08, 0.5, 0.08, 0.5, 1] # delay after end line

print(Fore.LIGHTBLACK_EX + "-----STAY-----") 

def write(music_lyric, delay):
    for (letter, vel, broke), d in zip(music_lyric, delay): 
        for char in letter:
            print(Style.BRIGHT + Fore.CYAN + char, end='', flush=True)
            
            time.sleep(vel)
        if broke:
            print()
            time.sleep(d)
        else:
            time.sleep(0.4)

write(music_lyric(), delays)