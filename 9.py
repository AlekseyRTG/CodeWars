# Make a program that filters a list of strings and returns a list with only your friends name in it.

# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

def friend(x):
    new_list = []
    i = 0
    # print(len(x))
    while i < len(x):
        if len(x[i]) == 4:
            # print(x[i])
            new_list.append(x[i])
        i += 1
    return new_list

print(friend(["Ryan", "Kieran", "Mark"]))