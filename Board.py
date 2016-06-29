# This class is meant to simulate a Pentago board which can be played on virtually.
# Author: Edgardo Gutierrez
# Class: TCSS 435
# Date: 3/13/16

class Board:

    # Instantiates an empty board ready for play.
    def __init__(self, firstPlayer):
        self.firstPlayer = firstPlayer
        if firstPlayer == 'w':
            self.secondPlayer = 'b'
        elif firstPlayer == 'b':
            self.secondPlayer = 'w'
        self.grid = [['.' for x in range(6)] for x in range(6)]
        self.heuristic = self.calculateHeuristic()
        self.whiteCount = 0
        self.blackCount = 0

    # Returns the grid object.
    def getGrid(self):
        return self.grid

    # Rotate the specified quadrant clockwise 90 degrees.
    def rotateClockwise(self, quadrant):
        # Top left
        if quadrant == 1:
                # Shift corners
                temp = self.grid[0][0]
                self.grid[0][0] = self.grid[0][2]
                self.grid[0][2] = self.grid[2][2]
                self.grid[2][2] = self.grid[2][0]
                self.grid[2][0] = temp

                # Shift edges
                temp = self.grid[0][1]
                self.grid[0][1] = self.grid[1][2]
                self.grid[1][2] = self.grid[2][1]
                self.grid[2][1] = self.grid[1][0]
                self.grid[1][0] = temp

        # Top right
        elif quadrant == 2:
                # Shift corners
                temp = self.grid[3][0]
                self.grid[3][0] = self.grid[3][2]
                self.grid[3][2] = self.grid[5][2]
                self.grid[5][2] = self.grid[5][0]
                self.grid[5][0] = temp

                # Shift edges
                temp = self.grid[3][1]
                self.grid[3][1] = self.grid[4][2]
                self.grid[4][2] = self.grid[5][1]
                self.grid[5][1] = self.grid[4][0]
                self.grid[4][0] = temp
        # Bottom left
        elif quadrant == 3:
                # Shift corners
                temp = self.grid[0][3]
                self.grid[0][3] = self.grid[0][5]
                self.grid[0][5] = self.grid[2][5]
                self.grid[2][5] = self.grid[2][3]
                self.grid[2][3] = temp

                # Shift edges
                temp = self.grid[0][4]
                self.grid[0][4] = self.grid[1][5]
                self.grid[1][5] = self.grid[2][4]
                self.grid[2][4] = self.grid[1][3]
                self.grid[1][3] = temp

        # Bottom right
        elif quadrant == 4:
                temp = self.grid[3][3]
                self.grid[3][3] = self.grid[3][5]
                self.grid[3][5] = self.grid[5][5]
                self.grid[5][5] = self.grid[5][3]
                self.grid[5][3] = temp

                # Shift edges
                temp = self.grid[3][4]
                self.grid[3][4] = self.grid[4][5]
                self.grid[4][5] = self.grid[5][4]
                self.grid[5][4] = self.grid[4][3]
                self.grid[4][3] = temp
        self.heuristic = self.calculateHeuristic()

    # Rotate the specified quadrant clockwise 90 degrees.
    def rotateCounterClockwise(self, quadrant):
        self.rotateClockwise(quadrant)
        self.rotateClockwise(quadrant)
        self.rotateClockwise(quadrant)

    # Add piece to board.
    def addPiece(self, quadrant, position, player):
        moveMade = True
        if quadrant == 1:
            if position == 1: moveMade = self.addToVacant((0,0), player)
            elif position == 2: moveMade = self.addToVacant((1,0), player)
            elif position == 3: moveMade = self.addToVacant((2,0), player)
            elif position == 4: moveMade = self.addToVacant((0,1), player)
            elif position == 5: moveMade = self.addToVacant((1,1), player)
            elif position == 6: moveMade = self.addToVacant((2,1), player)
            elif position == 7: moveMade = self.addToVacant((0,2), player)
            elif position == 8: moveMade = self.addToVacant((1,2), player)
            elif position == 9: moveMade = self.addToVacant((2,2), player)
            else: moveMade = False
        elif quadrant == 2:
            if position == 1: moveMade = self.addToVacant((3,0), player)
            elif position == 2: moveMade = self.addToVacant((4,0), player)
            elif position == 3: moveMade = self.addToVacant((5,0), player)
            elif position == 4: moveMade = self.addToVacant((3,1), player)
            elif position == 5: moveMade = self.addToVacant((4, 1), player)
            elif position == 6: moveMade = self.addToVacant((5,1), player)
            elif position == 7: moveMade = self.addToVacant((3,2), player)
            elif position == 8: moveMade = self.addToVacant((4,2), player)
            elif position == 9: moveMade = self.addToVacant((5,2), player)
            else: moveMade = False
        elif quadrant == 3:
            if position == 1: moveMade = self.addToVacant((0,3), player)
            elif position == 2: moveMade = self.addToVacant((1,3), player)
            elif position == 3: moveMade = self.addToVacant((2,3), player)
            elif position == 4: moveMade = self.addToVacant((0,4), player)
            elif position == 5: moveMade = self.addToVacant((1,4), player)
            elif position == 6: moveMade = self.addToVacant((2,4), player)
            elif position == 7: moveMade = self.addToVacant((0,5), player)
            elif position == 8: moveMade = self.addToVacant((1,5), player)
            elif position == 9: moveMade = self.addToVacant((2,5), player)
            else: moveMade = False
        elif quadrant == 4:
            if position == 1: moveMade = self.addToVacant((3,3), player)
            elif position == 2: moveMade = self.addToVacant((4,3), player)
            elif position == 3: moveMade = self.addToVacant((5,3), player)
            elif position == 4: moveMade = self.addToVacant((3,4), player)
            elif position == 5: moveMade = self.addToVacant((4,4), player)
            elif position == 6: moveMade = self.addToVacant((5,4), player)
            elif position == 7: moveMade = self.addToVacant((3,5), player)
            elif position == 8: moveMade = self.addToVacant((4,5), player)
            elif position == 9: moveMade = self.addToVacant((5,5), player)
            else: moveMade = False
        else: moveMade = False
        if moveMade:
            self.heuristic = self.calculateHeuristic()
            if player == 'w':
                self.whiteCount += 1
            elif player == 'b':
                self.blackCount += 1
        return moveMade

    # Adds a piece using the coordinate system.
    def addCoordinatePiece(self, coordinates, player):
        if self.addToVacant(coordinates, player):
            self.grid[coordinates[0]][coordinates[1]] = player
            self.heuristic = self.calculateHeuristic()
        else:
            print "ERROR IN addCoordinatePiece"

    # Returns the success of adding a piece to a space
    def addToVacant(self, coordinates, player):
        if self.grid[coordinates[0]][coordinates[1]] != '.':
            print "That position is occupied."
            return False
        else:
            self.grid[coordinates[0]][coordinates[1]] = player
            return True

    # Checks to see if a player has won.
    def checkForWin(self):
        blackWin = False
        whiteWin = False

        # Checks to see if either player has won in a row.
        for y in range(0, 6):
            blackCount = 0
            whiteCount = 0
            for x in range(0, 6):
                if self.grid[x][y] == 'b':
                    blackCount += 1
                elif self.grid[x][y] == 'w':
                    whiteCount += 1
            if (blackCount == 6):
                blackWin = True
            elif (whiteCount == 6):
                whiteWin = True
            elif (blackCount == 5 and (self.grid[0][y] != 'b' or self.grid[5][y] != 'b')):
                blackWin = True
            elif (whiteCount == 5 and (self.grid[0][y] != 'w' or self.grid[5][y] != 'w')):
                whiteWin = True

        # Checks to see if either player has won in a column.
        for x in range(0, 6):
            blackCount = 0
            whiteCount = 0
            for y in range(0, 6):
                if self.grid[x][y] == 'b':
                    blackCount += 1
                elif self.grid[x][y] == 'w':
                    whiteCount += 1
            if (blackCount == 6):
                blackWin = True
            elif (whiteCount == 6):
                whiteWin = True
            elif (blackCount == 5 and (self.grid[x][0] != 'b' or self.grid[x][5] != 'b')):
                blackWin = True
            elif (whiteCount == 5 and (self.grid[x][0] != 'w' or self.grid[x][5] != 'w')):
                whiteWin = True

        # Checks to see if either player has won in a diagonal from top
        # left to bottom right.
        blackCount = 0
        whiteCount = 0
        for num in range(0, 6):
            if self.grid[num][num] == 'b':
                blackCount += 1
            elif self.grid[num][num] == 'w':
                whiteCount += 1
        if (blackCount == 6):
            blackWin = True
        elif (whiteCount == 6):
            whiteWin = True
        elif (blackCount == 5 and (self.grid[0][0] != 'b' or self.grid[5][5] != 'b')):
            blackWin = True
        elif (whiteCount == 5 and (self.grid[0][0] != 'w' or self.grid[5][5] != 'w')):
            whiteWin = True

        # Checks to see if either player has won in a diagonal from top
        # left to bottom right shifted to the right one space.
        blackCount = 0
        whiteCount = 0
        for num in range(0, 5):
            if self.grid[num + 1][num] == 'b':
                blackCount += 1
            elif self.grid[num + 1][num] == 'w':
                whiteCount += 1
        if (blackCount == 5):
            blackWin = True
        elif (whiteCount == 5):
            whiteWin = True

        # Checks to see if either player has won in a diagonal from top
        # left to bottom right shifted to down one space.
        blackCount = 0
        whiteCount = 0
        for num in range(0, 5):
            if self.grid[num][num + 1] == 'b':
                blackCount += 1
            elif self.grid[num][num + 1] == 'w':
                whiteCount += 1
        if (blackCount == 5):
            blackWin = True
        elif (whiteCount == 5):
            whiteWin = True

        # Checks to see if either player has won in a diagonal from top
        # right to bottom left
        blackCount = 0
        whiteCount = 0
        for num in range(0, 6):
            if self.grid[5 - num][num] == 'b':
                blackCount += 1
            elif self.grid[5 - num][num] == 'w':
                whiteCount += 1
        if (blackCount == 6):
            blackWin = True
        elif (whiteCount == 6):
            whiteWin = True
        elif (blackCount == 5 and (self.grid[5][0] != 'b' or self.grid[0][5] != 'b')):
            blackWin = True
        elif (whiteCount == 5 and (self.grid[5][0] != 'w' or self.grid[0][5] != 'w')):
            whiteWin = True

        # Checks to see if either player has won in a diagonal from top
        # right to bottom left shifted to the left one space.
        blackCount = 0
        whiteCount = 0
        for num in range(0, 5):
            if self.grid[4 - num][num] == 'b':
                blackCount += 1
            elif self.grid[4 - num][num] == 'w':
                whiteCount += 1
        if (blackCount == 6):
            blackWin = True
        elif (whiteCount == 6):
            whiteWin = True
        elif (blackCount == 5):
            blackWin = True
        elif (whiteCount == 5):
            whiteWin = True

        # Checks to see if either player has won in a diagonal from top
        # right to bottom left shifted to the left one space.
        blackCount = 0
        whiteCount = 0
        for num in range(0, 5):
            if self.grid[5 - num][num + 1] == 'b':
                blackCount += 1
            elif self.grid[5 - num][num + 1] == 'w':
                whiteCount += 1
        if (blackCount == 6):
            blackWin = True
        elif (whiteCount == 6):
            whiteWin = True
        elif (blackCount == 5):
            blackWin = True
        elif (whiteCount == 5):
            whiteWin = True


        winner = None
        if blackWin and whiteWin:
            winner = "no one, it was a tie."
        elif blackWin:
            winner = "Black"
        elif whiteWin:
            winner = "White"
        return winner

    # Returns the overall board heuristic.
    def calculateHeuristic(self):
        if self.checkForWin() == "Black" and self.firstPlayer == 'b':
            return 100
        elif self.checkForWin() == "White" and self.firstPlayer == 'w':
            return -100
        return self.maxHeuristic() - self.minHeuristic()

    # Returns the first player bias heuristic.
    def maxHeuristic(self):
        total = 0
        # Check rows
        for y in range(0, 6):
            obstacles = 0
            for x in range(0, 6):
                if self.grid[x][y] == self.secondPlayer:
                    # Counts obstacles that would prevent max from winning
                    obstacles += 1
            # No obstacles, add 2 to the heuristic
            if obstacles == 0:
                total += 2
            elif obstacles == 1:
                if self.grid[0][y] == self.secondPlayer: total += 1
                elif self.grid[5][y] == self.secondPlayer: total += 1


        # Check cols
        for x in range(0, 6):
            obstacles = 0
            for y in range(0, 6):
                if self.grid[x][y] == self.secondPlayer:
                    # Counts obstacles that would prevent max from winning
                    obstacles += 1
            # No obstacles, add 2 to the heuristic
            if obstacles == 0:
                total += 2
            elif obstacles == 1:
                if self.grid[x][0] == self.secondPlayer: total += 1
                elif self.grid[x][5] == self.secondPlayer: total += 1

        # Check upper diagonal: Top left to bottom right
        obstacles = 0
        for num in range(0,5):
            if self.grid[num + 1][num] == self.secondPlayer:
                obstacles += 1
        if obstacles == 0:
            total += 1

        # Check lower diagonal: Top left to bottom right
        obstacles = 0
        for num in range(0,5):
            if self.grid[num][num + 1] == self.secondPlayer:
                obstacles += 1
        if obstacles == 0:
            total += 1

        # Check center diagonal: Top left to bottom right
        obstacles = 0
        for num in range(0,6):
            if self.grid[num][num] == self.secondPlayer:
                obstacles += 1
        if obstacles == 0:
            total += 2
        elif obstacles == 1:
            if self.grid[0][0] == self.secondPlayer: total += 1
            elif self.grid[5][5] == self.secondPlayer: total += 1

        # Check upper diagonal: Top right to bottom left
        obstacles = 0
        for num in range(0,5):
            if self.grid[4 - num][num] == self.secondPlayer:
                obstacles += 1
        if obstacles == 0:
            total += 1

        # Check lower diagonal: Top right to bottom left
        obstacles = 0
        for num in range(0,5):
            if self.grid[5 - num][num + 1] == self.secondPlayer:
                obstacles += 1
        if obstacles == 0:
            total += 1

        # Check center diagonal: Top right to bottom left
        obstacles = 0
        for num in range(0,6):
            if self.grid[5 - num][num] == self.secondPlayer:
                obstacles += 1
        if obstacles == 0:
            total += 2
        elif obstacles == 1:
            if self.grid[5][0] == self.secondPlayer: total += 1
            elif self.grid[0][5] == self.secondPlayer: total += 1

        # Total possible paths to win disregarding rotations
        return total

    # Returns the second player bias heuristic.
    def minHeuristic(self):
        total = 0
        # Check rows
        for y in range(0, 6):
            obstacles = 0
            for x in range(0, 6):
                if self.grid[x][y] == self.firstPlayer:
                    # Counts obstacles that would prevent min from winning
                    obstacles += 1
            # No obstacles, add 2 to the heuristic
            if obstacles == 0:
                total += 2
            elif obstacles == 1:
                if self.grid[0][y] == self.firstPlayer: total += 1
                elif self.grid[5][y] == self.firstPlayer: total += 1


        # Check cols
        for x in range(0, 6):
            obstacles = 0
            for y in range(0, 6):
                if self.grid[x][y] == self.firstPlayer:
                    # Counts obstacles that would prevent min from winning
                    obstacles += 1
            # No obstacles, add 2 to the heuristic
            if obstacles == 0:
                total += 2
            elif obstacles == 1:
                if self.grid[x][0] == self.firstPlayer: total += 1
                elif self.grid[x][5] == self.firstPlayer: total += 1

        # Check upper diagonal: Top left to bottom right
        obstacles = 0
        for num in range(0,5):
            if self.grid[num + 1][num] == self.firstPlayer:
                obstacles += 1
        if obstacles == 0:
            total += 1

        # Check lower diagonal: Top left to bottom right
        obstacles = 0
        for num in range(0,5):
            if self.grid[num][num + 1] == self.firstPlayer:
                obstacles += 1
        if obstacles == 0:
            total += 1

        # Check center diagonal: Top left to bottom right
        obstacles = 0
        for num in range(0,6):
            if self.grid[num][num] == self.firstPlayer:
                obstacles += 1
        if obstacles == 0:
            total += 2
        elif obstacles == 1:
            if self.grid[0][0] == self.firstPlayer: total += 1
            elif self.grid[5][5] == self.firstPlayer: total += 1

        # Check upper diagonal: Top right to bottom left
        obstacles = 0
        for num in range(0,5):
            if self.grid[4 - num][num] == self.firstPlayer:
                obstacles += 1
        if obstacles == 0:
            total += 1

        # Check lower diagonal: Top right to bottom left
        obstacles = 0
        for num in range(0,5):
            if self.grid[5 - num][num + 1] == self.firstPlayer:
                obstacles += 1
        if obstacles == 0:
            total += 1

        # Check center diagonal: Top right to bottom left
        obstacles = 0
        for num in range(0,6):
            if self.grid[5 - num][num] == self.firstPlayer:
                obstacles += 1
        if obstacles == 0:
            total += 2
        elif obstacles == 1:
            if self.grid[5][0] == self.firstPlayer: total += 1
            elif self.grid[0][5] == self.firstPlayer: total += 1

        # Total possible paths to win disregarding rotations
        return total

    # Returns an independant board clone of this board.
    def clone(self):
        cloneBoard = Board(self.firstPlayer)
        cloneBoard.grid = [['.' for x in range(6)] for x in range(6)]
        for y in range(0,6):
            for x in range(0,6):
                cloneBoard.grid[x][y] = self.grid[x][y]
        cloneBoard.heuristic = self.heuristic
        cloneBoard.firstPlayer = self.firstPlayer
        return cloneBoard

    # returns a list of tuples, each tuple contains a tuple of coordinates, player, quadrant and direction.
    def getPossibleActions(self):
        actions = []
        if self.whiteCount == self.blackCount:
            player = self.firstPlayer
        else:
            player = self.secondPlayer
        for y in range(0, 6):
            for x in range(0, 6):
                if self.grid[x][y] == '.':
                    for quadrant in range(1, 5):
                        for direction in range(0,2):
                            if direction == 0:
                                actions.append(((x,y), player, quadrant, 'l'))
                            elif direction == 1:
                                actions.append(((x,y), player, quadrant, 'r'))
        return actions

    # Returns a string for console display of the board.
    def __str__(self):
        # for action in self.getPossibleActions():
        #     print action
        display = "\nHeuristic: " + str(self.heuristic) + "\n+-------+-------+\n"
        for y in range(0, 6):
            for x in range(0, 6):
                if x == 0:
                    if y == 3:
                        display += "+-------+-------+\n"
                    display += "|"
                elif x == 3:
                    display += " |"
                display += " " + str(self.grid[x][y])
                if x == 5:
                    display += " |"
            display += "\n"
        display += "+-------+-------+\n"
        return display

    def getSnapshot(self):
        snapshot = ""
        for y in range(0,6):
            for x in range(0,6):
                snapshot += self.grid[x][y]
            if y != 5: snapshot += "\n"
        return snapshot
