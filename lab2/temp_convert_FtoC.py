#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""temp_convert.py: Convert temperature F to C."""

# initialize looping variable, assume yes as first answer
continueYN = "Y"

while continueYN.upper() == "Y":
    # get temperature input from the user, and prompt them for what we expect
    degF = float(input("Enter temperature in degrees Fahrenheit (°F) to convert: "))

    degC = (degF - 32) * 5 / 9

    # Round the floating point number to a single decimal place
    degC = round(degC, 1)

    print(f"Temperature in degrees C is: {degC}")

    # check for temperature below freezing...
    if degC < 0:
        print("Pack long underwear!")

    # check for it being a very hot day...
    if degF > 100:
        print("Remember to hydrate!")

    continueYN = input("Would you like to enter another (Y/N)? ")
