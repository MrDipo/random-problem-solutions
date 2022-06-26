from typing import List


def removeDuplicatesSet(stuff: List) -> List:
    stuff = set(stuff)
    return list(stuff)


things_around_me = ['mice', 'cup', 'phone', 27, 21, True, True, 21, 'mice', 'Mice', 'printer', 'printer']
print(removeDuplicatesSet(things_around_me))

# Extras
def removeDuplicatesSlow(stuff: List) -> List: 
    new_stuff = []
    for item in stuff:
        if item not in new_stuff:
            new_stuff.append(item)
    return new_stuff


print(removeDuplicatesSlow(things_around_me))