import cs50

def print_mario():
    hash = "#"
    emptySpace = " "
    gapLength = 2
    height = cs50.get_int("Height? ")

    # Prompt the user for the pyramid height
    if (height < 1 or height > 8):
        print_mario()
    else:
        # loop through the lines
        for i in range(1, height + 1):
            #loop through the columns
            for j in range(height * 2 + gapLength):
                # print left side of the pyramid
                if (j < height):
                    if (j < height - i):
                        print(" ", end="")
                    else:
                        print("#", end="")

                # print gap
                if (j > height and j < height + gapLength):
                    print("  ", end="")

                #print right side of the pyramid
                if (j >= height + gapLength and j < height + gapLength + i):
                   print("#", end="")

            print("")

print_mario()