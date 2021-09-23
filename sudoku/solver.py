def rowGenerator(dataList,maxRow):    
    rows = {}
    for i in range(maxRow):
        rows[f"row{i+1}"] = dataList[maxRow*(i):maxRow*(i+1)]        
    return rows
    
def solve(bo):    
    find = find_empty(bo) # 비어있는 칸의 위치를 찾음
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i    # 유효성 검사가 통과하는 경우 값을 할당

            if solve(bo):       # 새로운 bo와 함께 solve를 재귀적 호출
                return True     # 더 이상 비어있는 칸이 없다면 true를 반환 한다.

            bo[row][col] = 0    # 유효성 검사에 통과하지 못하면 false를 반환하게 되고 0이 할당됨

    return False

def valid(bo,num,pos): # num=입력될 숫자, pos(row,col)
    """
    행 체크
    bo[pos[0]][i] == num 부분은 해당 row의 전체에 입력될 값(num)이 존재하지 않는다면 유효성 통과함
    pos[1] != i 부분은 빈칸에 입력될 자기 자신을 제외한 경우
    """
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    """
    열 체크
    bo[i][pos[1]] == num 부분은 해당 col의 전체에 입력될 값(num)이 존재하지 않는다면 유효성 통과함
    pos[0] != i  부분은 빈칸에 입력될 자기 자신을 제외한 경우
    """
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    
    """    
    box는 9개의 정사각형 박스를 뜻함.
    해당 박스안에 입력값이 들어갈 수 있나 유효성 검사
    """
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
    dataList = [int(x) for x in dataList] # 문자열 데이터를 int형으로 변경
    rows = rowGenerator(dataList,9)       # 행단위로 리스트를 재배열   
    board = [rows[f"row{i}"] for i in range(1,10)] # 9행 9열로 재배열       
    solve(board)
    for i in board:
        print(i)
    return board