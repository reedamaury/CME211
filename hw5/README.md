The objective of this assignment was to develop a program in C++ that implements the right-hand wall following
algorithm to generate a solution path to a maze of arbitrary size. The program should ensure the number of command
line arguments are correct, confirm the static array has enough space to store the maze array, and then generate the
solution path to math, writing each adjacent move to an output file.

The solution path was generated via the aforementioned right-hand wall following algorithm. This algorithm is similar
to the state machine approach, in that it uses the current position and direction to decide the next move. For ease of
explanation, we will refer to the object that moves along the generated solution path, from cell to cell in the maze,
as a particle. In the program, the particle's current direction was denoted by the heading. The heading could take on
four directions/values:south (0), west (1), north (2), and east (3). Given the particle's current heading and position
in the maze, the algorithm instructs the particle to first attempt a right-turn, and if this is not possible continue in
the same direction. If it is not possible to turn right, or continue in the same direction, the algorithm will instruct
the particle to make a left turn. If the three aforementioned directions are not possible, the algorithm will instruct
the particle to make a u-turn. For example, when entering the maze on the top row, the particle's heading will be south.
Itwill begin by attempting to make a right turn and head west, and if that is not possible, it will continue heading
south. If neither of those headings are possible, the particle will attempt a left turn to the east, and if that is not
possible, then it will make a u-turn to the north. The algorithm was implemented via a series of sequential, conditional
else-if statements.

A Python program to validate the solution was also developed. The "check solution" program had 4 main objectives:
confirm the maze was entered at the correct location, confirm that solution does not go through any walls,
confirm each move is valid (meaning you can only move to adjacent cells), and lastly, confirm that solution exited the
maze at the correct location. To do this, the "check solution" program takes in the solution file and maze file and
implements a series of conditional if statements to test the veracity of conditions. If the aforementioned conditions,
were not violated, then the program prints "Solution is valid!"; if the conditions are violated, it will print
"Solution is not valid! ..." followed by the reason for the invalidity.