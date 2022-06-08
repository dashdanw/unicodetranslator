ASCII_UPPER_A = ord('A')
ASCII_LOWER_A = ord('a')

CIRCLED_UPPER_A = 0x24B6
CIRCLED_LOWER_A = 0x24D0

FULLWIDTH_UPPER_A = 0xFF21
FULLWIDTH_LOWER_A = 0xFF41



def generate_circled(input_text):
    output_text = ''
    for input_char in input_text:
        if input_char.islower():
            uni_char_code = ord(input_char) - ASCII_LOWER_A + CIRCLED_LOWER_A
            output_text += chr(uni_char_code)
        elif input_char.isupper():
            uni_char_code = ord(input_char) - ASCII_UPPER_A + CIRCLED_UPPER_A
            output_text += chr(uni_char_code)
        else:
            output_text += input_char
    return output_text


def generate_fullwidth(input_text):
    output_text = ''
    for input_char in input_text:
        if input_char.islower():
            uni_char_code = ord(input_char) - ASCII_LOWER_A + FULLWIDTH_LOWER_A
            output_text += chr(uni_char_code)
        elif input_char.isupper():
            uni_char_code = ord(input_char) - ASCII_UPPER_A + FULLWIDTH_UPPER_A
            output_text += chr(uni_char_code)
        else:
            output_text += input_char
    return output_text
