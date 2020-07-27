#Constants written here in case we want to change multiples or message
maxNum = 1000
lilMultiple = 3
bigMultiple = 5
lilWord = "Cyber"
bigWord = "Click"
BothWord = "Cyberclick"


for i in range(maxNum):
    # (i + 1) so we start counting on 1 and end in 1000
    j = i + 1
    # seems weird code but this way we only check for multiples of 15 once we already know we have a multiple of 5, therefore speeding it up a little bit
    if (j % bigMultiple == 0):
        if (j % lilMultiple == 0):
            print(f"{BothWord}")
        else:
            print(f"{bigWord}")
    elif (j % lilMultiple == 0):
        print(f"{lilWord}")
    else:
        print(f"{i + 1}")
