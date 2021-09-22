def rowGenerator(dataList,maxRow):    
    rows = {}
    for i in range(maxRow):
        rows[f"row{i+1}"] = dataList[maxRow*(i):maxRow*(i+1)]        
    return rows
    
def columnGenerator(rows,maxColumn):
    columns = {}    
    for i in range(maxColumn):
        list = []
        for v in rows.values():        
            list.append(v[i])        
        columns[f"col{i+1}"] = list        
    return columns


def rowCheck(row,number):        
    result = sorted(list(set(number) - set(row)))                
    return result
    

def colCheck(col,number):        
    result = sorted(list(set(number) - set(col)))
    return result
    
def current_possible_row_check(rows,possible_number,row_index,current_row_index):
    print(rows[f"row{row_index}"],str(possible_number).ljust(30),f"{row_index}행, {current_row_index+1}열")

def tableCheck(rows):
    print("="*14+"table"+"="*14)
    for i in range(9):
        print(f"row{i+1}",rows[f"row{i+1}"])
    print("="*15+"end"+"="*15)

def backtrackingAlgorithm(dataList):
    dataList = [int(x) for x in dataList]
    rows = rowGenerator(dataList,9)
    columns = columnGenerator(rows,9)
    number = list(x for x in range(1,10))    
        
    possible_number_list = []
    error_cnt = 0
    for row_index in range(1,10):
        loop = True        
        iop = 0 # pi: index of possible_number
        while loop:
            if 0 in rows[f"row{row_index}"]:
                row_number = rowCheck(rows[f"row{row_index}"],number)                
                current_row_index = rows[f"row{row_index}"].index(0)                
                possible_number = colCheck(columns[f"col{current_row_index+1}"],row_number)     
                try:
                    possible_number_list.append(possible_number)                    
                    # rows[f"row{row_index}"][current_row_index] = possible_number[iop]
                    # columns[f"col{current_row_index+1}"][row_index-1] = possible_number[iop]
                    rows[f"row{row_index}"][current_row_index] = possible_number_list[-1][iop]
                    columns[f"col{current_row_index+1}"][row_index-1] = possible_number_list[-1][iop]
                    current_possible_row_check(rows,possible_number,row_index,current_row_index)
                    iop = 0                    
                
                except IndexError:  
                    error_cnt += 1
                    print("error 발생 횟수",error_cnt)                         
                    print(possible_number_list[-2][iop])                                     
                    value = possible_number_list[-2][iop]
                    search_index = rows[f"row{row_index}"].index(value)
                    # search_index = rows[f"row{row_index}"].index(3)                    
                    rows[f"row{row_index}"][search_index] = 0
                    iop += 1                    
                    tableCheck(rows)
                    # print("test",rows[f"row{row_index}"])                   
                    # raise IndexError
                    pass
                           
            else:
                loop = False
    tableCheck(rows)           
    