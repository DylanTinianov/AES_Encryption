from constants import *


def rotate(word_32):
    tmp = word_32[0]
    word_32.pop(0)
    word_32.append(tmp)
    del tmp


def shift_row(_bytes, offset):
    for i in range(offset):
        rotate(word_32=_bytes)
