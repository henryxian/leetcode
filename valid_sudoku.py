# valid sudoku

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if len(board) != 9 or len(board[0]) != 9:
            return False

        for i in range(0, 9):
            flags = [False, ] * 10
            for j in range(0, 9):
                if board[i][j] == ".":
                    continue
                else:
                    index = int(board[i][j])
                    if flags[index] == False:
                        flags[index] = True
                    else:
                        return False

        for i in range(0, 9):
            flags = [False, ] * 10
            for j in range(0, 9):
                if board[j][i] == ".":
                    continue
                else:
                    index = int(board[j][i])
                    if flags[index] == False:
                        flags[index] = True
                    else:
                        return False

        #count = 0
        for offset1 in [0, 3, 6]:
            for offset2 in [0, 3, 6]:
                flags = [False, ] * 10
                #count = count + 1
                #print offset1, offset2
                for i in range(0 + offset1, 3 + offset1):
                    for j in range(0 + offset2, 3 + offset2):
                        if board[i][j] == ".":
                            continue
                        else:
                            index = int(board[i][j])
                            if flags[index] == False:
                                flags[index] = True
                            else:
                                return False
        #print "count: ", count
        #for i in range(6, 9):
        #    print
        #    for j in range(3, 6):
        #        print board[i][j],
        return True