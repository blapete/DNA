import random, sys, time

PAUSE = 0.08 

ROWS = [
    '         ##',
    '        #{}-{}#',
    '       #{}---{}#',
    '      #{}-----{}#',
    '     #{}------{}#',
    '    #{}------{}#',
    '    #{}-----{}#',
    '     #{}---{}#',
    '     #{}-{}#',
    '      ##',
    '     #{}-{}#',
    '     #{}---{}#',
    '    #{}-----{}#',
    '    #{}------{}#',
    '     #{}------{}#',
    '      #{}-----{}#',
    '       #{}---{}#',
    '        #{}-{}#']

try:
    print('Press Ctrl-C to quit...')
    time.sleep(2)
    rowIndex = 0

    while True:
        rowIndex = rowIndex + 1 # increment rowIndex to draw next row

        if rowIndex == len(ROWS):
            rowIndex = 0

        # row indexes 0 and 9 don't have nucleotides:
        if rowIndex == 0 or rowIndex == 9:
            print(ROWS[rowIndex])
            continue

        # random nucleotide pairs
        randomSelection = random.randint(1, 4)
        if randomSelection == 1:
            leftNucleotide, rightNucleotide = 'A', 'T'
        elif randomSelection == 2:
            leftNucleotide, rightNucleotide = 'T', 'A'
        elif randomSelection == 3:
            leftNucleotide, rightNucleotide = 'C', 'G'
        elif randomSelection == 4:
            leftNucleotide, rightNucleotide = 'G', 'C'

        print(ROWS[rowIndex].format(leftNucleotide, rightNucleotide))

        time.sleep(PAUSE)  # slight pause

except KeyboardInterrupt:
    sys.exit()
