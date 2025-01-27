# Write a function

# triple_double(num1, num2)
# which takes numbers num1 and num2 and returns 1 if there is a straight triple of a digit at any place in num1 and also a straight double of the same digit in num2.

# If this isn't the case, return 0

# Examples

# triple_double(451999277, 41177722899) == 1
# # num1 has straight triple 999s and num2 has straight double 99s

# triple_double(1222345, 12345) == 0
# # num1 has straight triple 2s but num2 has only a single 2

# triple_double(12345, 12345) == 0

# triple_double(666789, 12345667) == 1


def triple_double(num1, num2):
    # Convert num into str
    s1 = str(num1)
    s2 = str(num2)
    
    # Define the set of digits thah occur three in a row
    triples_in_num1 = set()
    for i in range(len(s1) - 2):
        if s1[i] == s1[i+1] == s1[i+2]:
            triples_in_num1.add(s1[i])
    
    # Check if there is the same number among the triples found in num1 which appears as two in a row in num2 
    for i in range(len(s2) - 1):
        if s2[i] == s2[i+1] and s2[i] in triples_in_num1:
            return 1  # Found a match 
    
    return 0  # If havent find any matching numbers


# Short solutions

def triple_double(num1, num2):
    for x in range(10):
        if str(x) * 3 in str(num1):
            if str(x) * 2 in str(num2):
                return 1
    return 0


def triple_double(num1, num2):
    return any([i * 3 in str(num1) and i * 2 in str(num2) for i in '0123456789'])