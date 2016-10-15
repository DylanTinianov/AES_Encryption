import key_schedule
from utils.used_functions import *
from utils.constants import *


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


class AesEncryption(object):
    def __init__(self):
        self.plain_text = str()
        self.encrypted_message = list()
        self.key = None

    def sub_bytes(self):
        for i in range(len(self.encrypted_message)):
            for j, num in enumerate(self.encrypted_message):
                self.encrypted_message[i][j] = s_box[num]

    def shift_rows(self, offset):
        for i in range(len(self.encrypted_message)):
            for j in range(len(self.encrypted_message)):
                shift_row(_bytes=self.encrypted_message[i][j], offset=offset)

    def mix_columns(self):
        pass

    def add_round_key(self):
        pass


#   For testing purposes
def main():
    message = _16byes("asdfghjklzxcvbnmqwertyuiop123456")
    for i in message:
        print i


if __name__ == '__main__':
    main()
