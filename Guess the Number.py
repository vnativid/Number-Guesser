#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 12:25:21 2021

@author: vincenatividad
"""

import random
#Guess the number (Computer)
def guess(x):
    random_number = random.randint(1, x) #between 1 and x
    guess = 0 
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number: 
            print ("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high.")
            
    print (f'You have guessed the number {random_number} correctly!')
guess(10) 

#Guess the number (Human)
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:  
            guess = random.randint(low, high)
        else:
            guess = low 
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)??').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
            
    print(f'Computer guessed your number, {guess} correctly.')
    
    
computer_guess(10)

