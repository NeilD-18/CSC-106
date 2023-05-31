# Kristina Striegnitz
# Fall 2020
#
# Play a simulated slot machine.

import random
from tkinter import W

def run_slot_machine(player_name):
    reel_1 = random.randint(1, 10)
    reel_2 = random.randint(1, 10)
    reel_3 = random.randint(1, 10)
    print("Reels show:", reel_1, reel_2, reel_3)

    if reel_1 == reel_2 and reel_1 == reel_3:
        print("You win, " + player_name + "!")
    else:
        print("Sorry, " + player_name + "! Maybe next time.")

def play_slot_machine():
   
    name = input("Welcome! What is your name?  ")
    
    while True:
    
        run_slot_machine(name)
    
        decision = str(input("Do you want to play again? (Y/N) "))
        
        if decision == "Y":
            run_slot_machine(name)
            
        else: 
            break 
        

play_slot_machine()
