#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""temp_convert.py: Convert temperature C to F."""


def convert_C_to_F(temp):
    # TODO: create conversion logic

# initialize looping variable, assume yes as first answer
continueYN = "Y"

while continueYN.upper() == "Y":
    # get temperature input from the user, and prompt them for what we expect
    degC = int(input("Enter temperature in degrees Celsius (°C) to convert: "))

    # TODO: Convert C to F (Formula: °F = °C * 9/5 + 32)
    # Call convert_C_to_F function

    # TODO: Print the results

    # check for temperature below freezing...
    # TODO: Print some helpful information for cold temperatures.


    # check for it being a very hot day...
    # TODO: Print some helpful information for hot temperatures.

    continueYN = input("Would you like to enter another (Y/N)? ")



