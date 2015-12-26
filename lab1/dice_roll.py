#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""dice_roll.py: Roll a pair of dice."""

import random
min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print "Rolling the dice..."
    print "The values are...."
    print random.randint(min, max)
    print random.randint(min, max)

    roll_again = raw_input("Would you like to roll the dice again?")

print "\nThanks for playing!"
