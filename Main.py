# This class runs the game loop and logic orchestration.
# Author: Edgardo Gutierrez
# Class: TCSS 435
# Date: 3/13/16

from Board import Board
from NPC import NPC
from random import randint
import re

def randomUserInput():
    quad1 = randint(1,4)
    quad2 = randint(1,4)
    position = randint(1,9)
    direction = randint(1,2)
    if direction == 1: direction = 'L'
    elif direction == 2: direction = 'R'
    return str(quad1) + "/" + str(position) + " " + str(quad2) + direction

def winnerIs(color):
    if color == "Black":
        if userColor == 'b':
            winStatement = "{} has won!, the champion is {}!".format(color, userName)
        else:
            winStatement = "{} has won!, the champion is the npc!".format(color)
    elif color == "White":
        if userColor == 'w':
            winStatement = "{} has won!, the champion is {}!".format(color, userName)
        else:
            winStatement = "{} has won!, the champion is the npc!".format(color)
    return winStatement

outputFile = open("PentagoOutput.txt", "w")
outputFile.write("PENTAGO OUTPUT\n\n")

# Choose name.
userName = raw_input("Please enter your name: ")

# Choose auto mode.
auto = raw_input("Would you like to play auto mode? Your input will be random. (Y/N): ")
if auto.lower() == 'y':
    auto = True
else:
    auto = False

# Choose color
userColor = raw_input("Please enter desired color(b/w): ").lower()
if userColor == 'w': npcColor = 'b'
elif userColor == 'b': npcColor = 'w'

# Random player start
if randint(1,2) == 1: currentPlayer = 'b'
else: currentPlayer = 'w'

# Set player statistcs.
firstPlayer = currentPlayer
if currentPlayer == userColor:
    firstPlayer = userName
    firstColor = userColor
    secondPlayer = "NPC"
    secondColor = npcColor
else:
    firstPlayer = "NPC"
    firstColor = npcColor
    secondPlayer = userName
    secondColor = userColor

# Instantiations
myBoard = Board(currentPlayer)
npc = NPC(npcColor, 3)
prompt = "> "
winner = None
movesMade = []

print myBoard

# Game loop
while (myBoard.blackCount + myBoard.whiteCount) < 36:
    outputFile.write("{}\n{}\n".format(firstPlayer, secondPlayer))
    outputFile.write("{}\n{}\n".format(firstColor.upper(), secondColor).upper())
    if currentPlayer == firstColor:
        outputFile.write("1\n")
    else:
        outputFile.write("2\n")
    outputFile.write("{}\n".format(myBoard.getSnapshot()))
    for move in movesMade:
        outputFile.write("{}\n".format(move))
    outputFile.write("\n")

    # print myBoard
    moveMade = False
    if currentPlayer == npcColor:
        print "NPC'S TURN"
    elif currentPlayer == userColor:
        print "{}'s TURN".format(userName)
    if currentPlayer == npcColor:
        playerInput = npc.getNPCInput(myBoard)
        npcInput = playerInput
    elif auto == True:
        playerInput = randomUserInput()
        userInput = playerInput
    else:
        playerInput = str(raw_input(prompt)).lower()
        userInput = playerInput

    # Quit
    if playerInput == "quit" or playerInput == "q":
        print "Bye!"
        break
    movesMade.append(playerInput)

    # Parsing input meaning.
    tokens = re.split("[/ ]", playerInput)
    placementQuadrant = int(tokens[0])
    placementPosition = int(tokens[1])
    rotationQuadrant = int(tokens[2][0])
    rotationDirection = tokens[2][1]

    # Adding Piece.
    moveMade = myBoard.addPiece(placementQuadrant, placementPosition, currentPlayer)
    winner = myBoard.checkForWin()
    if winner != None:
        print myBoard
        print winnerIs(winner)
        outputFile.write(winnerIs(winner))
        break

    if moveMade:
        # Rotating quadrant.
        if rotationDirection == 'r': myBoard.rotateClockwise(rotationQuadrant)
        elif rotationDirection == 'l': myBoard.rotateCounterClockwise(rotationQuadrant)
        winner = myBoard.checkForWin()
        if winner != None:

            print myBoard
            print winnerIs(winner)
            outputFile.write(winnerIs(winner))
            break

        # Switch current player.
        if currentPlayer == "w": currentPlayer = 'b'
        elif currentPlayer == "b": currentPlayer = 'w'
        print myBoard
if (myBoard.blackCount + myBoard.whiteCount) == 36:
    print "There was a tie, no one made a line of 5."
    outputFile.write("There was a tie, no one made a line of 5.")
outputFile.close()
