# !/u.sr/bin/env python3
# Created by: Angel
# Created on May 5,2025
# This program asks the user for their temperature in
# celsius and converts the temperature in fahrenheit.


def calculate_temp():
    # calculate temperature in fahrenheit
    try:
        # asks the user for their temperature
        user_temp = float(input("Enter the temperature in celsius (c): "))
        print("")

        # calculates the the temperature in fahrenheit
        temp_fahrenheit = (9 / 5) * user_temp + 32

        # prints out the output
        print("The temperature is {0} f".format(temp_fahrenheit))

    except:
        print("This cannot be ")


def main():
    # this function calls the other function

    # call function
    calculate_temp()


if __name__ == "__main__":
    main()
