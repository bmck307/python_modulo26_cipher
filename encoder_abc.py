import random

##This converts numbers to base 26 with 1 as 'a'
##I elected to do it this way since I wanted to multiply and anything multiplied by 0 is 0
def convert_and_multiply(split_input, split_input_length):
    for i in range(0,split_input_length):
        if split_input[i] != ' ':
            ## Checks if its lowercase
            if ord(split_input[i]) > 96 and ord(split_input[i]) < 123:
                split_input[i] = ord(split_input[i]) - 96
            ##Checks if its Uppercase
            elif ord(split_input[i]) > 64 and ord(split_input[i]) < 91:
                split_input[i] = ord(split_input[i]) - 64
            split_input[i] = (26 * random.randint(2, 50)) + split_input[i]
            
    return split_input

## This is effectively just an output function
## The neverending if/else is for formatting that i don't know how to do in python yet
def recombine(split_input, split_input_length):
    next = split_input[0]
    for i in range(0, split_input_length):
        if i + 1 < split_input_length:
            next = split_input[i + 1]
        if i == split_input_length - 1:
            print(str(split_input[i]))
        else:
            if next == ' ' or split_input[i] == ' ':
                print(str(split_input[i]), end="")
            else:
                print(str(split_input[i]), end ="/")

##This is a driver function for if I ever wanted to add steps or change the encoding
def encode_word(user_input):
    split_input = list(''.join(user_input))
    split_input_length = len(split_input)
    split_input = convert_and_multiply(split_input, split_input_length)
    recombine(split_input, split_input_length)

## This is effectively the start of my main method
user_input = input("What do you want to cipher (enter -1 to stop)? ")
while user_input != "-1":
    encode_word(user_input)
    user_input = input("What do you want to cipher (enter -1 to stop)? ")

