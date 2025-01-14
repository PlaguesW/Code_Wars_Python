# This kata is the first of a sequence of four about "Squared Strings".

# You are given a string of n lines, each substring being n characters long: For example:

# s = "abcd\nefgh\nijkl\nmnop"

# We will study some transformations of this square of strings.

# Vertical mirror: vert_mirror (or vertMirror or vert-mirror)
# vert_mirror(s) => "dcba\nhgfe\nlkji\nponm"
# Horizontal mirror: hor_mirror (or horMirror or hor-mirror)
#  hor_mirror(s) => "mnop\nijkl\nefgh\nabcd"
# or printed:

# vertical mirror   |horizontal mirror   
# abcd --> dcba     |abcd --> mnop 
# efgh     hgfe     |efgh     ijkl 
# ijkl     lkji     |ijkl     efgh 
# mnop     ponm     |mnop     abcd 
# Task:

# Write these two functions
# and

# high-order function oper(fct, s) where

# fct is the function of one variable f to apply to the string s (fct will be one of vertMirror, horMirror)

# Examples:

# s = "abcd\nefgh\nijkl\nmnop"
# oper(vert_mirror, s) => "dcba\nhgfe\nlkji\nponm"
# oper(hor_mirror, s) => "mnop\nijkl\nefgh\nabcd"
# Note:

# The form of the parameter fct in oper changes according to the language. You can see each form according to the language in "Sample Tests".

# Bash Note:

# The input strings are separated by , instead of \n. The output strings should be separated by \r instead of \n. See "Sample Tests".


def vert_mirror(strng):
    # Splitting text in a list of lines by line break characters
    lines = strng.split('\n')
    # For each line, we expand the sequence of characters
    reversed_lines = [line[::-1] for line in lines]
    # put it back together, separating it with a line break
    return '\n'.join(reversed_lines)

def hor_mirror(strng):
    # Split into a list of lines
    lines = strng.split('\n')
    # Reverse the order of lines
    lines.reverse()
    # Reverse the order of lines
    return '\n'.join(lines)

def oper(fct, s):
    # We apply the passed function (vert_mirror or hor_mirror) to the string s
    return fct(s)

#* Shortest solutions:
def vert_mirror(s):
    return "\n".join(line[::-1] for line in s.split("\n"))

def hor_mirror(s):
    return "\n",join(s.split("\n")[::-1])

def oper(fct, s):
    return fvt(s)