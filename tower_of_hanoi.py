# This solution shows the tracing of the function calls and also tells you
# how many moves were performed to solve the puzzle given the number of disks

A = []
B = []
C = []
indent_count = 0
moves = 0

n = int(input("num disks: "))

if ((type(n) == int) and (n > 0)):

    A = [i + 1 for i in range(n)] # peg size represented by number in list
    A = A[::-1] # order of numbers is largest to smallest


def move(n, start, end, bridge, indent_count):

    global moves
    indent_count += 1
    print(("    " * indent_count) + "ENTER", n)
    
    
    if n > 0:

        moves += 1
        
        print(("    " * indent_count) + "Calling move(" + str(n-1) + ", " +
              str(start) + ", " + str(bridge) + ", " + str(end) + ")")

        
        # Move n - 1 disks from start to end to free bottom one
        move(n - 1, start, bridge, end, indent_count)


        print(("    " * indent_count) + "Moving to " + str(end) +
              " from " + str(start))

        # Move disk #n to end from start
        end.append(start.pop())

        # Show current state of pegs
        print(("    " * indent_count) + "A = " + str(A) + " B = " + str(B) +
              " C = " + str(C))

        
        print(("    " * indent_count) + "Calling move(" + str(n-1) +
              ", " + str(bridge) + ", " +str(end) + ", " +
              str(start) + ")")
        
        # Move to end the n - 1 number of disks remaining on bridge
        move(n - 1, bridge, end, start, indent_count)

    print(("    " * indent_count) + "EXIT", n)
    indent_count -= 1
        



print("Calling move(" + str(n) + ", " + str(A) + ", " +
              str(C) + ", " + str(B))

#Call the function with start peg being A, end C and the bridge B
move(n, A, C, B, indent_count)

print("The number of moves =", moves)
