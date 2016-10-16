from aes_encryption import *
import operator


def run_encryption():
    encryption = AesEncryption()
    for round_num in range(1, NUM_ROUNDS+1):
        if round_num == 1:
            encryption.add_round_key()
        for method in ['sub_bytes', 'shift_rows', 'mix_columns', 'add_round_key']:
            if method == 'mix_columns' and round_num == 16:
                continue
            operator.methodcaller(method)(encryption)


def run_decryption():
    pass


def main():
    run_encryption()


if __name__ == '__main__':
    main()
