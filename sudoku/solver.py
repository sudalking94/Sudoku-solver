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

def remove_previous_value(possible_number_list,rows,row_index,columns):
    del possible_number_list[-1]
    previous_value =  list(set(possible_number_list[-1]) & set(rows[f"row{row_index}"]))[0]                                            
    search_index = rows[f"row{row_index}"].index(previous_value)                                   
    rows[f"row{row_index}"][search_index] = 0
    columns[f"col{search_index+1}"][row_index-1] = 0    
    

def backtrackingAlgorithm(dataList):
    dataList = [int(x) for x in dataList]
    rows = rowGenerator(dataList,9)
    columns = columnGenerator(rows,9)
    number = list(x for x in range(1,10))    
        
    possible_number_list = []
    
    for row_index in range(1,10):
        loop = True                
        while loop:
            if 0 in rows[f"row{row_index}"]:
                row_number = rowCheck(rows[f"row{row_index}"],number)                
                current_row_index = rows[f"row{row_index}"].index(0)                
                possible_number = colCheck(columns[f"col{current_row_index+1}"],row_number)                     
                possible_number_list.append(possible_number)                
                                
                if len(possible_number) != 0:                    
                    rows[f"row{row_index}"][current_row_index] = possible_number_list[-1][0]
                    columns[f"col{current_row_index+1}"][row_index-1] = possible_number_list[-1][0]
                    current_possible_row_check(rows,possible_number,row_index,current_row_index)

                elif len(possible_number) == 0:                    
                    remove_previous_value(possible_number_list,rows,row_index,columns)                    
                    tableCheck(rows)                    
                    if 0 in rows[f"row{row_index}"]:
                        current_row_index = rows[f"row{row_index}"].index(0)
                    
                    
                    i = 1
                    while True:
                        if len(possible_number_list[-1]) == 1:
                            remove_previous_value(possible_number_list,rows,row_index,columns)
                            if 0 in rows[f"row{row_index}"]:
                                current_row_index = rows[f"row{row_index}"].index(0)
                            continue
                        print("while 다음행",possible_number_list[-1])
                        
                            
                        print("i",i)
                        rows[f"row{row_index}"][current_row_index] = possible_number_list[-1][i]
                        columns[f"col{current_row_index+1}"][row_index-1] = possible_number_list[-1][i]
                        print("첫 번째 대입 가능한 숫자",possible_number_list[-1])
                        current_possible_row_check(rows,possible_number_list[-1],row_index,current_row_index)

                        row_number = rowCheck(rows[f"row{row_index}"],number)                
                        current_row_index = rows[f"row{row_index}"].index(0)                
                        possible_number = colCheck(columns[f"col{current_row_index+1}"],row_number)                     
                        possible_number_list.append(possible_number)

                        if len(possible_number) == 0:
                            remove_previous_value(possible_number_list,rows,row_index,columns)
                            if 0 in rows[f"row{row_index}"]:
                                current_row_index = rows[f"row{row_index}"].index(0)                                                  
                            i += 1 # possible_number에 다음 값이 존재하는 경우 index 증가
                            if i >= len(possible_number_list[-1]): # possible_number_list[-1] 의 배열길이보다 i가 큰 경우 그 이전의 값을 제거
                                i = 0
                                # del possible_number_list[-1]
                                print("두 번째 대입 가능한 숫자",possible_number_list[-2])                                
                                remove_previous_value(possible_number_list,rows,row_index,columns)
                                print("두 번째 대입 가능한 숫자를 지운후 행의 값들",rows[f"row{row_index}"])
                                if 0 in rows[f"row{row_index}"]:
                                    current_row_index = rows[f"row{row_index}"].index(0)
                                    i += 1
                                continue
                        else:
                            del possible_number_list[-1]
                            break
                # rows[f"row{row_index}"][current_row_index] = possible_number_list[-1][iop]
                # columns[f"col{current_row_index+1}"][row_index-1] = possible_number_list[-1][iop]
                # current_possible_row_check(rows,possible_number,row_index,current_row_index)                
                                                                                          
            else:
                loop = False
    tableCheck(rows)           
    