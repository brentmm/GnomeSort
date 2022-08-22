from random import randint


#generates list if 10 random numbers
def test():
    a = []
    for i in range(0, 10):
        a.append(randint(0, 10))
    return a

#sorts list of random numbers
def gnomeSort(c):
    n = len(c)
    place = 0
    count = 0
    while place < n:
        count += 1
        if place == 0:
            place = place + 1 # moved forward if at begining of list
        else:
            if c[place] < c[place - 1]: #compares values
                c[place], c[place - 1] = c[place - 1], c[place] #swaps numbers
                place = place - 1 #goes back to previous index
            else:
                place = place + 1 #moves forward if no swap

    return c, count

#driver code
b = test()
print("Original: " + str(b))
d = gnomeSort(b)
print()
print("Sorted: " + str(d[0]))
print("Output: " + str(d[1]))
