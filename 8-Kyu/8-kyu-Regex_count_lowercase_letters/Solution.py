# DESCRIPTION:
#
# Your task is simply to count the total number of lowercase letters in a string.
#
# Examples:
#
# "abc" ===> 3
# "abcABC123" ===> 3
# "abcABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~" ===> 3
# "" ===> 0;
# "ABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~" ===> 0
# "abcdefghijklmnopqrstuvwxyz" ===> 26

def lowercase_count(strng):
    count = 0
    for i in strng:
        if i.islower():
            count += 1
    return count