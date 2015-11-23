import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()

def ascii_to_binary(message):
    result = ""
    
    for c in message:
        bin_c = bin(ord(c))[2:]
        result += bin_c.zfill(7)
    
    #print(message, " encoded in binary is:", result, file=sys.stderr)
    return result


def get_repetitions(my_string, my_char):
    repetitions = 0
    
    for i in range(len(my_string)):
        if(my_string[i] == my_char):
            repetitions += 1
        else:
            break
    
    #print("repetitions of ", my_char , " in ", my_string, " = ", repetitions, file=sys.stderr)    
    return repetitions
    
#print("received message =", message, file=sys.stderr)
message_bits = ascii_to_binary(message)

encoded_message = ""

i = 0

while (i < len(message_bits)):
    m_bit = message_bits[i]
    
    encoded_message += "0"
    
    if (m_bit == "0"):
        encoded_message += "0"
        
    encoded_message += " "
    
    repetitions = get_repetitions(message_bits[i:], m_bit)
    
    encoded_message += ("0" * repetitions)
    
    i += repetitions
    
    if (i < len(message_bits)):
        encoded_message += " "
    
print(encoded_message)