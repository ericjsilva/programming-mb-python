#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""temp_convert.py: Convert temperature F to C."""

# initialize looping variable, assume yes as first answer
continueYN = "Y"

while continueYN.upper() == "Y":
    # get temperature input from the user, and prompt them for what we expect
    degF = int(raw_input("Enter temperature in degrees Fahrenheit (°F) to convert: "))

    degC = (degF - 32) * 5/9

    print "Temperature in degrees C is: {temp}".format(temp=degC)

    # check for temperature below freezing...
    if degC < 0:
        print "Pack long underwear!"

    # check for it being a very hot day...
    if degF > 100:
        print "Remember to hydrate!"

    continueYN = raw_input("Would you like to enter another (Y/N)? ")



