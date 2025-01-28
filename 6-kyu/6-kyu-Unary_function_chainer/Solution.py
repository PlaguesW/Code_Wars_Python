# Your task is to write a higher order function for chaining together a list of unary functions. In other words, it should return a function that does a left fold on the given functions.

# chained([a,b,c,d])(input)
# Should yield the same result as

# d(c(b(a(input))))

def chained(functions):
    def func(arg):
        # Start with the initial argument
        result = arg
        # Apply each function in the list sequentially
        for f in functions:
            result = f(result)  # Apply the current function to the result
        return result
    return func


# Shortest sol

def chained(functions):
    return lambda x : chained(functions[1:])(functions[0](x)) if functions else x