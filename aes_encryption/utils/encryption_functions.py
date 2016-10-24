from constants import *


def rotate(word_32):
    tmp = word_32[0]
    word_32.pop(0)
    word_32.append(tmp)
    del tmp
    return word_32


def shift_row(_bytes, offset):
    for i in range(offset):
        _bytes = rotate(word_32=_bytes)
    return _bytes


def mix_col_multiply(vector_, count):
    if count == 0:
        return multiply_2[vector_[0]], multiply_3[vector_[1]], vector_[2], vector_[3]
    elif count == 1:
        return vector_[0], multiply_2[vector_[1]], multiply_3[vector_[2]], vector_[3]
    elif count == 2:
        return vector_[0], vector_[1], multiply_2[vector_[2]], multiply_3[vector_[3]]
    else:
        return multiply_3[vector_[0]], vector_[1], vector_[2], multiply_2[vector_[3]]


def mix_col_multiply_inv(vector_, count):
    if count == 0:
        return multiply_14[vector_[0]], multiply_11[vector_[1]], multiply_13[vector_[2]], multiply_9[vector_[3]]
    elif count == 1:
        return multiply_9[vector_[0]], multiply_14[vector_[1]], multiply_11[vector_[2]], multiply_13[vector_[3]]
    elif count == 2:
        return multiply_13[vector_[0]], multiply_9[vector_[1]], multiply_14[vector_[2]], multiply_11[vector_[3]]
    else:
        return multiply_11[vector_[0]], multiply_13[vector_[1]], multiply_9[vector_[2]], multiply_14[vector_[3]]
