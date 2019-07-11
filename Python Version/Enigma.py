# Enigma Machine Emulator
# by Justin Oxford
#
#
# This program emulates the Enigma Machine used by Germany in WWII.
# There are 3 wheels, with 26 slots per wheel, each corresponding to a letter (a-z). The numbers 0-25 correspond to
# the respective letter in the standard alphabet with a=0, b=1,... z=25. The first wheel turns after each character,
# the second wheel turns after each turn of the first wheel, and the third wheel turns after each turn of the second.
#
# I have not added in the ability to re-wire inputs (which was a feature of the German military Enigma Machines). The
# reason behind this is ease-of-use (I didn't feel like putting in 16 inputs before I send a message while testing.
# This version is far more simple (and more easily cracked), but it is the same as what commercially sold Enigmas would
# have offered in terms of encryption. Later versions may feature changeable character pairs - it would be quit easy to
# implement as it would simply be a user generated list/array taken from inputs and then an extra bit in the circuit.
# Additionally, the input is only taken in strings with letters a-z and no spaces. While I considered adding the ability
# to type freely with more characters and spaces, this is not how the original machine operated.
#
#
########################################################################################################################
########################################################################################################################
########################################################################################################################
#
# Import Modules =======================================================================================================

import time

# Create Wheels ========================================================================================================
# THESE VALUES MUST BE SHARED WITH RECIPIENT FOR MESSAGE TO BE UN-SCRAMBLED.
wheel_a = [15, 6, 19, 7, 22, 13, 9, 16, 3, 8, 0, 14, 10, 17, 4, 24, 18, 12, 5, 21, 25, 23, 20, 11, 2, 1]
wheel_b = [11, 22, 16, 1, 9, 13, 23, 24, 20, 17, 6, 25, 0, 3, 14, 18, 15, 8, 5, 4, 7, 21, 19, 12, 2, 10]
# DO NOT TOUCH THE VALUES BELOW, IF YOU DO, CHANGES MUST BE MADE IN PAIRS!!!
wheel_c = [18, 19, 21, 13, 8, 11, 12, 23, 24, 3, 5, 7, 20, 6, 4, 1, 22, 15, 16, 10, 14, 2, 17, 9, 25, 0]
scrambl = [17, 12, 24, 19, 21, 15, 25, 8, 7, 23, 16, 14, 1, 18, 11, 5, 10, 0, 13, 3, 22, 4, 20, 9, 2, 6]
# THESE VALUES MUST REMAIN IDENTICAL TO THE DESIRED INITIAL SETTING (0,0,0)
wheel_a_reset = [15, 6, 19, 7, 22, 13, 9, 16, 3, 8, 0, 14, 10, 17, 4, 24, 18, 12, 5, 21, 25, 23, 20, 11, 2, 1]
wheel_b_reset = [11, 22, 16, 1, 9, 13, 23, 24, 20, 17, 6, 25, 0, 3, 14, 18, 15, 8, 5, 4, 7, 21, 19, 12, 2, 10]
wheel_c_reset = [18, 19, 21, 13, 8, 11, 12, 23, 24, 3, 5, 7, 20, 6, 4, 1, 22, 15, 16, 10, 14, 2, 17, 9, 25, 0]
scrambl_reset = [17, 12, 24, 19, 21, 15, 25, 8, 7, 23, 16, 14, 1, 18, 11, 5, 10, 0, 13, 3, 22, 4, 20, 9, 2, 6]


# Define Variables =====================================================================================================

run_program = True

# ======================================================================================================================


# get the specific settings for wheel a, b, c -- note, must be same as encrypted STARTING point to decode.
def get_wheel_settings(wheel_a, wheel_b, wheel_c):

    while True:
        try:
            wheel_a_init = int(input("Wheel A Setting: "))
            for i in range(wheel_a_init):
                x = wheel_a[0]
                wheel_a.append(x)
                wheel_a.pop(0)
        except ValueError:
            print("Invalid Entry, must be a number.")
            continue
        if wheel_a_init > 25 or wheel_a_init < 0:
            print("Invalid Entry, must be between 0 and 25")
            continue
        else:
            break

    while True:
        try:
            wheel_b_init = int(input("Wheel B Setting: "))
            for i in range(wheel_b_init):
                x = wheel_b[0]
                wheel_b.append(x)
                wheel_b.pop(0)
        except ValueError:
            print("Invalid Entry, must be a number.")
            continue
        if wheel_b_init > 25 or wheel_b_init < 0:
            print("Invalid Entry, must be between 0 and 25")
            continue
        else:
            break

    while True:
        try:
            wheel_c_init = int(input("Wheel C Setting: "))
            for i in range(wheel_c_init):
                x = wheel_c[0]
                wheel_c.append(x)
                wheel_c.pop(0)
        except ValueError:
            print("Invalid Entry, must be a number.")
            continue
        if wheel_c_init > 25 or wheel_c_init < 0:
            print("Invalid Entry, must be between 0 and 25")
            continue
        else:
            break

    return wheel_a_init, wheel_b_init, wheel_c_init


# this converts the string entered into an array of numbers
def char_to_number(message_array):
    numeration_array = []
    slot = 0
    for letter in message_array:  # convert letters 'a' through 'z' into numbers 0 through 25
        numeration = ord(letter) - 97
        numeration_array.insert(slot, numeration)
        slot += 1
    return numeration_array


# this function does the encryption/decoding
def encrypt(wheel_a, wheel_b, wheel_c, message_numeration):
    iterations = 0
    code_message_array = []
    for code in message_numeration:  # run the message through the gears
        a = wheel_a[code]
        b = wheel_b[a]
        c = wheel_c[b]
        d = scrambl.index(c)
        e = wheel_c.index(d)
        f = wheel_b.index(e)
        g = wheel_a.index(f)
        code_letter = wheel_a.index(f)
        code_message_array.append(code_letter)

        iterations += 1
        wheel_b_turn = iterations % 26
        wheel_c_turn = iterations % (26 * 26)

        a_first = wheel_a[0]
        wheel_a.append(a_first)
        wheel_a.pop(0)

        if wheel_b_turn == 0:
            b_first = wheel_b[0]
            wheel_b.append(b_first)
            wheel_b.pop(0)
        if wheel_c_turn == 0:
            c_first = wheel_c[0]
            wheel_c.append(c_first)
            wheel_c.pop(0)
            scram_first = wheel_c[0]
            scrambl.append(scram_first)
            scrambl.pop(0)

    return code_message_array

# this turns the new array of numbers into characters a-z
def numbers_to_english(code_message_num):
    slot_rev = 0
    numbers_to_letters_array = []
    for letter in code_message_num:  # change the numbers back to letters
        numeration = chr(letter + 97)
        numbers_to_letters_array.insert(slot_rev, numeration)
        slot_rev += 1
    return numbers_to_letters_array


# Run the machine ======================================================================================================

print("#############################")
print("WELCOME TO THE ENIGMA MACHINE")
print("#############################")

while run_program is True:

    run = input("Do you want to run the machine?(y/n) ").lower()

    if run == 'y':

        wheel_setting = get_wheel_settings(wheel_a, wheel_b, wheel_c)
        while True:
            try:
                message_input = str(input("What is your secret message (no spaces, letters only)? ")).lower()
            except ValueError:
                print("That is not a valid message. Remove all spaces and only use letters a to z.")
                continue
            else:
                break

        message_array = list(message_input)
        message_length = len(message_input)
        message_numeration = char_to_number(message_array)
        code_message_num = encrypt(wheel_a, wheel_b, wheel_c, message_numeration)
        message_characterization = numbers_to_english(code_message_num)
        result = ''.join(message_characterization)

        print("#################################################")
        time.sleep(1)
        print("Generating...")
        time.sleep(1)
        print("#################################################")
        print("#################################################")
        print("")
        print("Here is your message:")
        print("-------------------------------------------------")
        print(f"Message        : {result}")
        print(f"Wheel settings : {wheel_setting}")
        print("-------------------------------------------------")

        # reset the wheels to 0, 0, 0
        wheel_a = wheel_a_reset
        wheel_b = wheel_b_reset
        wheel_c = wheel_c_reset
    elif run == 'n':
        print("Program ending... destroy all records.")
        time.sleep(2)
        run_program = False

    else:
        print("ERROR. That is not a valid entry.")