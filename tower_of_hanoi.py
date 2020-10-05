##Question 11 (Bonus):
##
##The idea of the puzzle is that you have three
##pegs and a set of disks where each disk is a different size. The goal
##is to move all of the disks(i.e., 3) from peg 1 to peg 3 while not
##violating the following rules:
##
##1. You may only move 1 disk at a time.
##2. A larger disk cannot be placed on top of a smaller disk.
##3. All disks must be on some peg except the disk in-transit.

peg1 = []
peg2 = []
peg3 = []

num_disks = int(input('How many disks are in this puzzle?: '))


if ((type(num_disks) == int) and (num_disks > 0)):

    print(num_disks)

    peg1 = [i + 1 for i in range(num_disks)] # peg size represented by number in list
    peg1 = peg1[::-1] # order of numbers is largest to smallest

    count = 0;
    i = 0;
    j = 1;

    pegs = [peg1, peg2, peg3] #2d array for the pegs
    
    if num_disks % 2 == 0:

        while count != 15: #len(peg3) != num_disks:

            if i > 2:
                i = 0
                print("i is 0")

            if j > 2:
                j = 0
                

            if not pegs[1]:#pegs[i][-1] < max(pegs[j]):
                
                pegs[j].append(pegs[i].pop())
                count += 1

            elif pegs[1]:
                print('pegs[%d] : %s' % (j, pegs[j]))

                if pegs[i][-1] < max(pegs[j]):
                    pegs[j].append(pegs[i].pop())
                    count += 1

            if not pegs[2]:
                pegs[2].append(pegs[i].pop())
                count += 1

            elif pegs[2]:
                pegs[2].append(pegs[i].pop())
                count += 1;
                
            print(pegs)
            i += 1
            #j += 1
            
