import key_schedule
from utils.used_functions import *
from utils.constants import *
import operator


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


def run_encryption():
    encryption = AesEncryption()
    for round_num in range(1, NUM_ROUNDS+1):
        if round_num == 1:
            encryption.add_round_key()
        for method in ['sub_bytes', 'shift_rows', 'mix_columns', 'add_round_key']:
            if method == 'mix_columns' and round_num == 16:
                continue
            operator.methodcaller(method)(encryption)


class AesDecryption(object):
    def __init__(self):
        pass


def run_decryption():
    pass


#   For testing purposes
def main():
    message = _16byes("asdfghjklzxcvbnmqwertyuiop123456")
    for i in message:
        print i


if __name__ == '__main__':
    main()
