# The numbers in the columns of a Bingo ticket are selected at random and printed according to the range 
# - in the B column are from 1 to 15
# - in the I column between 16 and 30
# - in the N column (that contains four numbers and the free (blank) space) between 31 and 45
# - in the G column between 46 and 60
# - in the O column between 61 and 75.

# No number can be repeated. 
# The numbers must be organized from smallest to largest in each column.

# Create a bingo card generator in any data type you like. 
# A dictionary of lists:
# bingo_card = {
#     b_col: [1,2,3,4,5],
#     i_col: [16,17,18,19,20],
#     n_col: [31,32,'free',34,35],
#     g_col: [46,47,48,49,50],
#     o_col: [66,67,68,69,70],
# }
# One long list:
# bingo_card = [1,2,3,4,5,16,17,18,19,20,31,32,'free',34,35,46,47,48,49,50,66,67,68,69,70]

# an object with a list
# bingo_card.b_col = [1,2,3,4,5]
# bingo_card.c_col = [16,17,18,19,20]
# etc.

# As a bonus, you can print them to the screen in bingo format

import random
import collections



random.randint(1,15)
random.randint(16,30)
random.randint(31,45)
random.randint(46,60)
random.randint(61,75)

bingo_card = {
    'b_col': [1,2,3,4,5],
    'i_col': [16,17,18,19,20],
    'n_col': [31,32,'free',34,35],
    'g_col': [46,47,48,49,50],
    'o_col': [66,67,68,69,70]
}

def gen(lo, hi, free):
    col = ((random.sample(xrange(lo, hi), 5)))
    if free:
        col[2] = '*' 
    return col

card = []

card.append(gen(1, 15, False))
card.append(gen(16, 30, False))
card.append(gen(31, 45, True))
card.append(gen(46, 60, False))
card.append(gen(61, 75, False))

def card_printer():
    print "    B   |   I   |   N   |   G   |   O   "
    print " ---------------------------------------"

    for i in range(0,5):
        print '|',
        for col in card:
            col[i] = str(col[i])
            if len(col[i]) == 1:
                col[i] = '  ' + col[i] + '   |'
            else:
                col[i] = ' ' + col[i] + '   |'
            print col[i],
        print ''
