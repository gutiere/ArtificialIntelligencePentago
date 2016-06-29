# This class is meant to simulate a Pentago player.
# Author: Edgardo Gutierrez
# Class: TCSS 435
# Date: 3/13/16

from random import randint
class NPC:
    # Instantiates a NPC which will play Pentago.
    def __init__(self, color, terminalDepth):
        self.color = color
        self.terminalDepth = terminalDepth
        self.depth = 0

    # Returns a string of input that follows the proper format.
    def getNPCInput(self, board):
        # coordinates, player, quadrant and direction
        action = self.alphaBetaSearch(board)
        # print "ACTION CHOSEN: ", action
        if action != None:
            posQuad = self.coordinateToPosQuad(action[0])
            quad1 = posQuad[1]
            quad2 = action[2]
            position = posQuad[0]
            direction = action[3]
        else:
            print "RANDOM NPC MOVE"
            quad1 = randint(1,4)
            quad2 = randint(1,4)
            position = randint(1,9)
            direction = randint(1,2)
            if direction == 1: direction = 'L'
            elif direction == 2: direction = 'R'
        return str(quad1) + "/" + str(position) + " " + str(quad2) + direction

    # Implements Alpha-Beta-Pruning to make an educated action based on the scope.
    def alphaBetaSearch(self, board):
        self.nodesExpanded = 0
        value = self.maxValue(board, -100000000, 100000000)
        print "Nodes Expanded: ", self.nodesExpanded
        print "Terminal Depth: ", self.terminalDepth
        for action in board.getPossibleActions():
            if value == self.result(board, action).heuristic:
                return action
        return None

    # Alpha-Beta-Pruning helper method.
    def maxValue(self, board, alpha, beta):
        self.nodesExpanded += 1
        if self.depth == self.terminalDepth:
            return board.heuristic
        value = -100000000
        self.depth += 1
        for action in board.getPossibleActions():
            value = max(value, self.minValue(self.result(board, action), alpha, beta))
            if value >= beta: return value
            alpha = max(alpha, value)
        self.depth -= 1
        return value

    # Alpha-Beta-Pruning helper method.
    def minValue(self, board, alpha, beta):
        self.nodesExpanded += 1
        if self.depth == self.terminalDepth:
            return board.heuristic
        value = 100000000
        self.depth += 1
        for action in board.getPossibleActions():
            value = min(value, self.maxValue(self.result(board, action), alpha, beta))
            if value <= alpha: return value
            beta = min(beta, value)
        self.depth -= 1
        return value

    # Returns a board after an action has been applied.
    def result(self, board, action):
        newBoard = board.clone()
        newBoard.addCoordinatePiece(action[0], action[1])
        if action[3] == 'r':
            newBoard.rotateClockwise(action[3])
        elif action[3] == 'l':
            newBoard.rotateCounterClockwise(action[3])
        return newBoard

    # Converts a basic coordinate based system to quadrant and position.
    def coordinateToPosQuad(self, coordinate):
        x = coordinate[0]
        y = coordinate[1]
        if x < 3 and y < 3:
            quad = 1
        elif x >= 3 and y < 3:
            quad = 2
        elif x < 3 and y >= 3:
            quad = 3
        elif x >= 3 and y >= 3:
            quad = 4
        pos = (x % 3) + 1 + ((y % 3) * 3)
        return (pos, quad)
