#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 13:16:30 2020

@author: Tuomas Jalonen
"""

"""
Someone once said 'The Collatz Conjecture is a really infamous conjecture
which wastes both time and energy.'

So here is my contribution to this nonsense! I saw a news article about it and
decided to code this function for fun.
"""

import time

def main():
    """
    This function calculates the Collatz Conjecture steps and wasted computing
    time and prints them.
    
    The idea is shortly this:
        Check if the input number is positive integer
        Repeat until you reach number 1:
            If the number is even:
                Divide by 2
            If the number is odd:
                Multiply by 3 and add 1
                
    If the conjecture holds true, the result should be one for all positive 
    integers.

    Returns
    -------
    None.

    """
    while True:
        num = input("Choose positive integer: ")
        try:
            num = int(num)
            if num < 1:
                print('The number is not a positive integer. Please try again.')
                continue
            break
        except ValueError:
            print('The number is not an integer. Please try again.')   
    start_time = time.time()
    
    i = 0
    print('Number:', num)
    
    while num != 1:
        if (num % 2) == 0:
            num /= 2
        else:
            num = 3 * num + 1
        i += 1
        print('Step:', i, 'Result:', int(num))
        
    if num == 1:
        print('You reached 1 i.e. the conjecture still holds true.')
        print('If you want to get a Nobel prize, you should keep trying with other numbers!')
        print('Computing time wasted:', time.time() - start_time, 'seconds')
    
main()