# This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!

# All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

# What is considered Valid?

# A string of braces is considered valid if all braces are matched with the correct brace.

# Examples

# "(){}[]"   =>  True
# "([{}])"   =>  True
# "(}"       =>  False
# "[(])"     =>  False
# "[({})](]" =>  False

def valid_braces(string):
    if string.find("{") == True and string.find("}") == True:
        return True
    else:
        return False
    if string.find("(")  and string.find(")") != -1:
        return True
    else:
        return False
    if string.find("[") != -1 and string.find("]") != -1:
        return True
    else:
        return False
    pass

print(valid_braces("(){}[]"))