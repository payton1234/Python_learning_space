#!/usr/bin/env python3
#Rock, Paper, Scissors! Loser jumps into the water!
import random

if __name__ == "__main__":
    choices = ["Rock", "paper", "scissors"]
    #問使用者要不要玩剪刀石頭布
    print("Do you want to play papper, scissors, stone? Loser jumps into the water.")
    answer = input()
    #如果說好:
    if answer == "yes":
        print("Nice, let's play!")
        user_choice = int(input("Rock = 0, Papper = 1, scissors = 2\n"))
        if 0 <= user_choice <= 2:
            cpu_choice = random.randint(0, 2)
            print("user: ", choices[user_choice])
            print("cpu: ", choices[cpu_choice])
            if user_choice == cpu_choice:
                print("Draw!")
            elif user_choice > cpu_choice and user_choice - cpu_choice == 1:
                print("You won! I am jumping now :(")
            elif user_choice < cpu_choice and user_choice - cpu_choice == 2:
                print("You won! I am jumping now :(")
            else:
                print("You lost! Jump!")
        else:
            print("Illegal choice")
    else:
        print("Bye bye")    
