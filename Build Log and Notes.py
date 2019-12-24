'''
BUILD NOTES - TO DO

Square Evaluator
	Needs to have a fresh Copy of MASTER ARRAY

add a "solver that compares with how far you are from solving
make the game have expandable size
read in high score, name and date
get high score and current score working
get rid of old versions
start numbering settings versions
be more careful when refactoring - do more checking.
make pieces different colors
make a piece a different size.
____________________________________________________________________
TileBreaker 2.4 -
fixed part of the high score tracker - it now knows when done and records if a score is better than high score.
completed first phase of distance checker -
The idea is that each piece to be solved will be featured in the center of the board.
I will need to use a copy of the MASTER_ARRAY

____________________________________________________________________
TileBreaker 2.3 -
Fixed corner counting issues
fixed pull highlights
fixed rotate highlights
learned to not use pngs made on older versions of photoshop
____________________________________________________________________


TIP - 2D ARRAY VERTICAL / HORIZONTAL SWAP
for w in range (5):
    for l in range (5):
        numcheck = MASTERLIST [l][w]
        print (numcheck)

TIP - BUILD PIECES LIKE AN ASSEMBLY LINE WHEN SETTING UP MULTIPLE PARTS -
GETTING ALL OF THE SETUP LISTS OF THIS PROJECT WAS A CHALLENGE.
USING AN 'EMPTY LIST' IN EACH STEP LIKE THE CURRENT STEP ON AN ASSEMBLY LINE REALLY HELPED.
'''
