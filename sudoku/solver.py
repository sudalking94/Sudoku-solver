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


def backtrackingAlgorithm(dataList):
    dataList = [int(x) for x in dataList]
    rows = rowGenerator(dataList,9)
    columns = columnGenerator(rows,9)
    number = tuple(x for x in range(1,10))    
        
    for tableIndex in range(1,10):        
        for i in range(len(number)):
            if number[i] in rows[f"row{tableIndex}"]:            
                continue
            else:
                if number[i] in columns[f"col{tableIndex}"]:                
                    continue
                else:
                    """
                    다 성공하는 경우 number를 배열에 넣어야 함
                    set list ? 둘중 어느 것이 더 빠른가?
                    """
                    pass