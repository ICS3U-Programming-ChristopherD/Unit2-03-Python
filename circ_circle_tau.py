#!/usr/bin/env python3

# Created By: Chris Di Bert
# Date: Sep. 26, 2022
# This program calculates the circumference of a circle using tau and user-inputted dimensions.

import constants


def main():
    user_choice = int(
        input("Enter 1 if you'd like to enter the radius of the circle: ")
    )
    print("")
    if user_choice == 1:
        radius = float(input("Enter the radius of the circle: "))
        circumference = radius * constants.TAU
        print(f"The circumference of the circle is {circumference}cm.")

    else:
        diameter = float(input("Enter the diameter of the circle:"))
        print("")
        circumference = (diameter / 2) * constants.TAU
        print(f"The circumference of the circle is {circumference}cm.")


if __name__ == "__main__":
    main()
