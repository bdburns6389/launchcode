import random


# The roll_dice function simulates the rolling of the dice. It
# creates a 2 dimensional list: each column is a die and each
# row is a throw. The function generates random numbers 1-6
# and puts them in the list.
def roll_dice(num_dice, num_rolls):

    # create a two-dimensional (num_dice by num_rolls) of zeros
    double_list = [[0 for i in range(num_dice)] for j in range(num_rolls)]

    # loop through each row and column, filling it with a random roll
    for roll in range(0, len(double_list)):
        for die in range(0, len(double_list[roll])):
            double_list[roll][die] = (int)(random.random()*6 + 1)

    return double_list


print (roll_dice(3, 2))