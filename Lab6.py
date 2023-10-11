#Nickholas Campos-Bautista


class BadValueError(Exception):
    def __init__(self, value):
        self.value = value
#create a class to take exceptions

def main():
    print("\nWelcome to the password Encoder and Decoder!")
    keep_asking = True
    while keep_asking:
        print("\nWhat operation would you like to perform?")
        print("1. Encode a password")
        print("2. Decode a password")
        print("3. Quit")
#initiate a loop that will continue printing menu
        try:
            user_choice = int(input("\n-->\t"))
            #ask the user for their choice
            if user_choice == 1:
                encode()
            elif user_choice == 2:
                pass
            elif user_choice == 3:
                keep_asking = False
            else:
                raise BadValueError("Option out of Range")
                #raise error if input is out of range
        except (BadValueError, ValueError):
            print("Bad input, try again...")
            continue
        #handle exceptions if input is bad


def encode():
    print("\nWhat code do you need to encode?")
    un_encoded_num = input("-->\t")
    final_encoded_string = ""
    #get initial password and initiate empty string
    for num in un_encoded_num:
        num = int(num)
        num += 3
        #get every number and add 3 to it
        if num > 9:
            num -= 10
        #if it ends up over 9, subtract 10
        final_encoded_string += str(num)
        #add it to the final string
    print(f"\nEncoded Password: {final_encoded_string}")
    #print final number


#--------------------
#decoder goes here :)
#--------------------


if __name__ == '__main__':
    main()