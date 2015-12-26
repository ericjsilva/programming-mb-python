#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""temp_convert.py: Convert temperature C to F."""

# initialize looping variable, assume yes as first answer
continueYN = "Y"

while continueYN.upper() == "Y":
    # get temperature input from the user, and prompt them for what we expect
    degF = int(raw_input("Enter temperature in degrees Fahrenheit (°C) to convert: "))

    # TODO: Convert C to F

    # TODO: Print the results

    # check for temperature below freezing...
    # TODO: Print some helpful information for cold temperatures.


    # check for it being a very hot day...
    # TODO: Print some helpful information for hot temperatures.

    continueYN = raw_input("Would you like to enter another (Y/N)? ")



