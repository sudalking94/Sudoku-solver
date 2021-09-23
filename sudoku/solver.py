def rowGenerator(dataList,maxRow):    
    rows = {}
    for i in range(maxRow):
        rows[f"row{i+1}"] = dataList[maxRow*(i):maxRow*(i+1)]        
    return rows
    
def solve(bo):    
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False

def valid(bo,num,pos): # num=입력될 숫자, pos(row,col)
    # 행 체크
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # 열 체크
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

def find_empty(bo):
    for x in range(len(bo)):
        for y in range(len(bo)):
            if bo[x][y] == 0:
                return (x,y)
    return None

def backtrackingAlgorithm(dataList):
    dataList = [int(x) for x in dataList]    
    rows = rowGenerator(dataList,9)    
    board = [rows[f"row{i}"] for i in range(1,10)]    
    for i in board:
        print(i)
    print("="*30)
    solve(board)
    for i in board:
        print(i)