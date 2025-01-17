# You need to write a password generator that meets the following criteria:

# 6 - 20 characters long
# contains at least one lowercase letter
# contains at least one uppercase letter
# contains at least one number
# contains only alphanumeric characters (no special characters)
# Return the random password as a string.

# Note: "randomness" is checked by counting the characters used in the generated passwords - all characters should have less than 50% occurance. Based on extensive tests, the normal rate is around 35%.

#* Solution without libs
def password_gen(counter=0):
    def pseudo_rand(seed):
        return (seed * 214013 + 2531011) & 0x7FFFFFFF
    
    def pick_rand(seed, chars):
        index = seed % len(chars)
        return chars[index]

    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    all_chars = lower + upper + digits

    import time
    seed = (int(time.time() * 1e9) + counter) & 0x7FFFFFFF

    seed = pseudo_rand(seed)
    password_length = 6 + (seed % 15)

    password = []

    seed = pseudo_rand(seed)
    password.append(pick_rand(seed, lower))
    seed = pseudo_rand(seed)
    password.append(pick_rand(seed, upper))
    seed = pseudo_rand(seed)
    password.append(pick_rand(seed, digits))

    while len(password) < password_length:
        seed = pseudo_rand(seed)
        password.append(pick_rand(seed, all_chars))

    for i in range(len(password)):
        seed = pseudo_rand(seed)
        j = seed % len(password)
        password[i], password[j] = password[j], password[i]

    return "".join(password)

for i in range(10):
    print(password_gen(counter=i))
    
    
#* Solution with libs

from string import ascii_lowercase as LOWER, ascii_uppercase as UPPER, digits as DIGITS
from random import choice, shuffle, randint

def password_gen():
    pw = [choice(UPPER), choice(LOWER), choice(DIGITS)] + [choice(UPPER+LOWER+DIGITS) for i in range(randint(3, 17))]
    shuffle(pw)
    return "".join(pw)

#* Another solution

from random import randint, choice
def password_gen():
    check = randint(6, 20)
    password = ''
    while len(password)<check:
        password += choice('abcdefghijklmnopqrstuvwxyz')
        password += choice('abcdefghijklmnopqrstuvwxyz'.upper())
        password += choice('0123456789')
    return password[:check]