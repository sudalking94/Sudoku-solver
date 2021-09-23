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

def removed_value_and_init_value(possible_number_list,rows,row_index,columns):
    del possible_number_list[-1]
    previous_value =  list(set(possible_number_list[-1]) & set(rows[f"row{row_index}"]))[0]                                                
    possible_number_list[-1].remove(previous_value)    
    search_index = rows[f"row{row_index}"].index(previous_value)                                   
    rows[f"row{row_index}"][search_index] = 0
    columns[f"col{search_index+1}"][row_index-1] = 0
    return possible_number_list[-1]
    

def backtrackingAlgorithm(dataList):
    dataList = [int(x) for x in dataList]
    rows = rowGenerator(dataList,9)
    columns = columnGenerator(rows,9)
    number = list(x for x in range(1,10))    
        
    possible_number_list = []
    init_row_index = 1
    row_number = rowCheck(rows[f"row{init_row_index}"],number)
    current_row_index = rows[f"row{init_row_index}"].index(0)                
    possible_number = colCheck(columns[f"col{current_row_index+1}"],row_number)                     
    possible_number_list.append(possible_number)

    # cnt = 0                
    for row_index in range(1,10):
        init_row_index = row_index
        loop = True
        while loop:
        # while cnt < 5:
            # cnt += 1
            # print("cnt",cnt)
            if 0 in rows[f"row{row_index}"]:                                                                
                if len(possible_number_list[-1]) != 0:
                    current_row_index = rows[f"row{row_index}"].index(0)
                    rows[f"row{row_index}"][current_row_index] = possible_number_list[-1][0]
                    columns[f"col{current_row_index+1}"][row_index-1] = possible_number_list[-1][0]
                    current_possible_row_check(rows,possible_number,row_index,current_row_index)                    
                    possible_number = list(filter(lambda x:x != possible_number_list[-1][0],possible_number_list[-1]))
                    print(possible_number)
                    possible_number_list.append(possible_number)


                elif len(possible_number) == 0:                    
                    removed_value_and_init_value(possible_number_list,rows,row_index,columns)                    
                    
                tableCheck(rows)        
                                                                                          
            else:
                loop = False
    tableCheck(rows)           
    