class Solution:

    def check_duplicate(self, alist):
            elements = []
            for i in range(len(alist)):
                if alist[i] != '.':
                    if alist[i] not in elements:
                        elements.append(alist[i])
                    else:
                        return False
            return True 
        
    def get_all_boxes(self, board):
        all_boxes = []
        i = 0
        while i<len(board):
            temp = []
            temp.append(board[i][:3])
            temp.append(board[i+1][:3])
            temp.append(board[i+2][:3])
            all_boxes.append(temp)

            temp = []
            temp.append(board[i][3:6])
            temp.append(board[i+1][3:6])
            temp.append(board[i+2][3:6])
            all_boxes.append(temp)

            temp = []
            temp.append(board[i][6:9])
            temp.append(board[i+1][6:9])
            temp.append(board[i+2][6:9])
            all_boxes.append(temp)

            i = i + 3
        return all_boxes
    
    
    def check_all_rows(self, board):
        for i in range(len(board)):
            result = self.check_duplicate(board[i])
            if result == False:
                return result
        return result
    
    def check_all_columns(self, board):
        for c in range(len(board)):
            alist = []
            for r in range(len(board)):
                alist.append(board[r][c])
            result = self.check_duplicate(alist)
            if result == False:
                return result
        return result
    
    
    def check_all_boxes(self, board):
        all_boxes = self.get_all_boxes(board)
        for i in range(len(all_boxes)):
            x = all_boxes[i]
            y =[]
            for i in range(3):
                for j in range(3):
                    y.append(x[i][j])

            result = self.check_duplicate(y)
            if result == False:
                return result
        return result


    def isValidSudoku(self, board: list[list[str]]) -> bool:
        result1, result2, result3 = self.check_all_rows(board), self.check_all_columns(board), self.check_all_boxes(board)
        if result1 == False or result2 == False or result3 == False:
            return False
        return True
            
        
        

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

        
sol = Solution()

print(sol.isValidSudoku(board))