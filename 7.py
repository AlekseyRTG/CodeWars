# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.
def likes(name):
    length = len(name)
    number = length - 2
    if length > 3:
        # print(name[0] + ', ' +  name[1] + ' and' + ' ' + str(number) + ' others like this')
        like = name[0] + ', ' +  name[1] + ' and' + ' ' + str(number) + ' others like this'
    elif length == 0:
        # print('no one likes this')
        like = 'no one likes this'
    elif length == 3:
        # print(name[0] + ', ' + name[1] +' and ' + name[2] + ' like this')
        like =  name[0] + ', ' + name[1] +' and ' + name[2] + ' like this'
    elif length == 2:
        # print(name[0] + ' and ' + name[1] + ' likes this')
        like =  name[0] + ' and ' + name[1] + ' likes this'
    else:
        # print(name[0] + ' likes this')
        like = name[0] + ' likes this'
    return like

likes([])