# DESCRIPTION:
# Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each.
# If one of the flowers has an even number of petals and the ither has an odd number of petals it means they are in love.

def lovefunc( flower1, flower2 ):
    if flower1 % 2 ==1 and flower2 % 2 == 0:
        return True
    if flower1 % 2 == 0 and flower2 % 2 == 1:
        return True
    else:
        return False

# shorter version

def lovefunc( flower1, flower2 ):
    if flower1 % 2 == 0 and flower2 % 2 != 0 or flower1 % 2 != 0 and flower2 % 2 == 0:
        return True
    else:
        return False