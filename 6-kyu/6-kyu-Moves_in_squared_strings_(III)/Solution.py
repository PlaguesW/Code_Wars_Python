# You are given a string of n lines, each substring being n characters long: For example:

# s = "abcd\nefgh\nijkl\nmnop"

# We will study some transformations of this square of strings.

# Let's now transform this string!

# Symmetry with respect to the main diagonal: diag_1_sym (or diag1Sym or diag-1-sym)
# diag_1_sym(s) => "aeim\nbfjn\ncgko\ndhlp"
# Clockwise rotation 90 degrees: rot_90_clock (or rot90Clock or rot-90-clock)
# rot_90_clock(s) => "miea\nnjfb\nokgc\nplhd"
# selfie_and_diag1(s) (or selfieAndDiag1 or selfie-and-diag1) It is initial string + string obtained by symmetry with respect to the main diagonal.
# s = "abcd\nefgh\nijkl\nmnop" --> 
# "abcd|aeim\nefgh|bfjn\nijkl|cgko\nmnop|dhlp"
# or printed for the last:
# selfie_and_diag1
# abcd|aeim
# efgh|bfjn
# ijkl|cgko 
# mnop|dhlp
# Task:

# Write these functions diag_1_sym, rot_90_clock, selfie_and_diag1
# and

# high-order function oper(fct, s) where

# fct is the function of one variable f to apply to the string s (fct will be one of diag_1_sym, rot_90_clock, selfie_and_diag1)

# Examples:

# s = "abcd\nefgh\nijkl\nmnop"
# oper(diag_1_sym, s) => "aeim\nbfjn\ncgko\ndhlp"
# oper(rot_90_clock, s) => "miea\nnjfb\nokgc\nplhd"
# oper(selfie_and_diag1, s) => "abcd|aeim\nefgh|bfjn\nijkl|cgko\nmnop|dhlp"
# Notes:

# The form of the parameter fct in oper changes according to the language. You can see each form according to the language in "Your test cases".

# It could be easier to take these katas from number (I) to number (IV)

# Bash Note: The output strings should be separated by \r instead of \n. See "Sample Tests".


def rot_90_clock(strng):
    if not strng:
        return ""
    lines = strng.split('\n')
    n = len(lines)
    # Transpose the matrix and unfold each row
    rotated = [''.join([lines[n - j - 1][i] for j in range(n)]) for i in range(n)]
    return '\n'.join(rotated)

def diag_1_sym(strng):
    if not strng:
        return ""
    lines = strng.split('\n')
    n = len(lines)
    transposed = [''.join([lines[j][i] for j in range(n)]) for i in range(n)]
    return '\n'.join(transposed)

def selfie_and_diag1(strng):
    if not strng:
        return ""
    diag = diag_1_sym(strng)
    original_lines = strng.split('\n')
    diag_lines = diag.split('\n')
    # Combine strings through |
    combined = [f"{original_lines[i]}|{diag_lines[i]}" for i in range(len(original_lines))]
    return '\n'.join(combined)

def oper(fct, s):
    return fct(s)


# Short solution

def rot_90_clock(strng):
    return '\n'.join(''.join(x) for x in zip(*strng.split('\n')[::-1]))      
def diag_1_sym(strng):
    return '\n'.join(''.join(x) for x in zip(*strng.split('\n'))) 
def selfie_and_diag1(strng):
    return '\n'.join('|'.join(x) for x in zip(strng.split('\n'), diag_1_sym(strng).split('\n')))
def oper(fct, s):
    return fct(s)
