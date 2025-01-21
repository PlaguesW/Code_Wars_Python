# EEE 754 is a standard for representing floating-point numbers (i.e. numbers that can have a fractional part and emulate real numbers).

# Its use is currently ubiquitous in both software (programming languages implementations) and hardware (Floating Point Units (FPU) chips embedded in processors).

# The 2 most widely used IEEE 754 formats are called the single precision (SP, encoded on 32 bits) and double precision (DP, encoded on 64 bits) formats.

# In C/C++, these correspond respectively to the types float and double, in virtually every implementation that supports floating-point numbers
# The default Python implementation, CPython, is written in C and represents Python floats internally as C doubles, and thus as IEEE 754 DP
# In JavaScript, all Numbers are IEEE 754 DP values.
# In Rust, these correspond respectively to the types f32 and f64.
# In Java, these correspond respectively to the types float and double.
# Before Lua 5.3, all numbers were IEEE 754 DP. Since Lua 5.3, numbers can be either IEEE 754 DP or 2's complement integers.
# As you can see on the images below, IEEE 754 numbers are divided into 3 fields :

# a sign bit;
# an exponent encoded on 8 (SP) or 11 (DP) bits;
# a mantissa (also called significand) encoded on 23 (SP) or 52 (DP) bits.
# The IEEE 754 single-precision encoding schemeThe IEEE 754 double-precision encoding scheme
# Your task is to write a function that takes as input a floating point number, and returns the binary IEEE 754 encoding of this number as a string, with fields separated by spaces for readability. If your programming language supports both SP and DP, you will have 2 functions to write, one for each type.

# Example

# Single Precision
# input:
# 15.875
# output:
# "0 10000010 11111100000000000000000"
# Double Precision
# input:
# 15.875
# output:
# "0 10000000010 1111110000000000000000000000000000000000000000000000"
# Note

# If you find yourself writing overly complex code, you are probably on the wrong path. Your solution should only be concerned with the bit-pattern of the number, without dealing with its value.

# Related Katas

# If you want to solve the same problem with a different approach, try :

# Float to Binary Conversion (in Javascript)
# This kata was inspired by this very interesting C kata :

# C Puzzle: Extract Field from a Double Value
# My kata about classifying floating-point numbers:

# Classify a floating point number

# Надо выполнить это задание, используя даннуб функциб:
# def float_to_IEEE_754(f : float) -> str:
#     return ""


import numpy as np

def float_to_IEEE_754(f: float, precision: str = 'DP') -> str:
    if precision == 'SP':
        as_int = np.float32(f).view(np.int32)
        sign = (as_int >> 31) & 0b1
        exponent = (as_int >> 23) & 0b11111111
        mantissa = as_int & 0b11111111111111111111111
        return f"{sign} {format(exponent, '08b')} {format(mantissa, '023b')}"
    elif precision == 'DP':
        as_int = np.float64(f).view(np.int64)
        sign = (as_int >> 63) & 0b1
        exponent = (as_int >> 52) & 0b11111111111
        mantissa = as_int & 0b1111111111111111111111111111111111111111111111111111
        return f"{sign} {format(exponent, '011b')} {format(mantissa, '052b')}"


# Short way

from struct import pack
s = "{:08b}".format

def float_to_IEEE_754 (f : float) -> str :
    binary = ''.join(map(s, pack('!d', f)))
    return ' '.join((binary[0], binary[1:12], binary[12:]))

# Another way

import ctypes

def float_to_IEEE_754 (f : float) -> str :
    s = bin(ctypes.c_ulong.from_buffer(ctypes.c_double(f)).value)[2:]
    s = (64-len(s))*'0' + s
    return s[0] + ' ' + s[1:12] + ' ' + s[12:]

# One more

import struct

def float_to_IEEE_754(x):
    val = struct.unpack('Q', struct.pack('d', x))[0]
    return b' '.join(struct.unpack('s 11s 52s', format(val, '064b').encode())).decode()