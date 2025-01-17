# Description

# Your job is to create a simple password validation function, as seen on many websites.

# The rules for a valid password are as follows:

# There needs to be at least 1 uppercase letter.
# There needs to be at least 1 lowercase letter.
# There needs to be at least 1 number.
# The password needs to be at least 8 characters long.
# You are permitted to use any methods to validate the password.

# Examples:

# password("Abcd1234"); ===> true
# password("Abcd123"); ===> false
# password("abcd1234"); ===> false
# password("AbcdefGhijKlmnopQRsTuvwxyZ1234567890"); ===> true
# password("ABCD1234"); ===> false
# password("Ab1!@#$%^&*()-_+={}[]|\:;?/>.<,"); ===> true;
# password("!@#$%^&*()-_+={}[]|\:;?/>.<,"); ===> false;
# Extra info

# You will only be passed strings.
# The string can contain any standard keyboard character.
# Accepted strings can be any length, as long as they are 8 characters or more.

def password(st):
    if len(st) < 8:
        return False
    
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    
    for char in  st:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
            
    if has_uppercase and has_lowercase and has_digit:
        return True
    
    return False
            


# Short solution

Param = (str.islower, str.isupper, str.isdigit)

def password(st):
    return len(st) > 7 and any (all(map(f, st)) for f in Param)

# Another solution

def password(string):
    if len(string) >= 8:
        check = 0
        for c in string:
            if   c.isupper(): check |= 1
            elif c.islower(): check |= 2
            elif c.isdigit(): check |= 4
            if check == 7: return True
    return False