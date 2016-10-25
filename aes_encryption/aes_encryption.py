import key_schedule
from utils import *


class AesEncryption(object):
    def __init__(self):
        self.encrypted_message = list()
        self.key = None

    def sub_bytes(self):
        for i in range(len(self.encrypted_message)):
            for j, num in enumerate(self.encrypted_message[i]):
                self.encrypted_message[i][j] = s_box[num]

    def shift_rows(self):
        for i in range(len(self.encrypted_message)):
            offset = 0
            for part in range(0, 16, 4):
                self.encrypted_message[i][part:part + 4] = \
                    shift_row(_bytes=self.encrypted_message[i][part:part+4], offset=offset)
                offset += 1

    def mix_columns(self):
        for i in range(len(self.encrypted_message)):
            count = 0
            for part in range(0, 16, 4):
                self.encrypted_message[i][part:part + 4] = \
                    mix_col_multiply(vector_=self.encrypted_message[i][part:part + 4], count=count)
                count += 1

    def add_round_key(self):
        pass

    def __str__(self):
        for i in self.encrypted_message:
            print i
        print


class AesDecryption(object):
    def __init__(self):
        self.encrypted_message = list()
        self.key = None

    def sub_bytes_inv(self):
        for i in range(len(self.encrypted_message)):
            for j, num in enumerate(self.encrypted_message[i]):
                self.encrypted_message[i][j] = inverse_s_box[num]

    def shift_rows_inv(self):
        for i in range(len(self.encrypted_message)):
            offset = 0
            for part in range(0, 16, 4):
                self.encrypted_message[i][part:part + 4] = \
                    shift_row_inv(_bytes=self.encrypted_message[i][part:part+4], offset=offset)
                offset += 1

    def mix_columns_inv(self):
        for i in range(len(self.encrypted_message)):
            count = 0
            for part in range(0, 16, 4):
                self.encrypted_message[i][part:part + 4] = \
                    mix_col_multiply_inv(vector_=self.encrypted_message[i][part:part + 4], count=count)
                count += 1

    def add_round_key_inv(self):
        pass

    def __str__(self):
        for i in self.encrypted_message:
            print i
        print


#   For testing purposes
def test():
    encryption = AesEncryption()
    encryption.encrypted_message = bytes_16('asdfghjklzxcvbnmqwertyuiop123456')
    encryption.__str__()

    encryption.sub_bytes()
    encryption.__str__()

    print "Shit Rows"
    encryption.shift_rows()
    encryption.__str__()

    print "mix cols"
    encryption.mix_columns()
    encryption.__str__()


if __name__ == '__main__':
    test()
