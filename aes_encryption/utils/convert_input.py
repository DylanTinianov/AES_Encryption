import os


def obtain_input():
    data_file = open(os.path.join(os.path.dirname(__file__), 'message/message_to_encrypt.txt'), "r")
    out = open(os.path.join(os.path.dirname(__file__), 'message/encrypted_text.txt'), "r+")
    data = list()

    for line in data_file:
        data.append(line.split())
    for i in range(len(data)):
        for n in range(len(data[i])):
            data[i][n] += " "


def text_convert(plain_text):
    bit_message = list()
    for char in plain_text:
        bit_message.append(ord(char))
    return bit_message


def _16byes(plain_text):
    message = list()
    for i in range(0, len(plain_text), 16):
        message.append(text_convert(plain_text[i:i+16]))

    for i in message:
        while len(i) < 16:
            i.append(0)
    return message
