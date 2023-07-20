_line_ = int(input())
_column_ = int(input())
_matrizNum_ = []
_max_line = []
_max_column = []
_mainList_ = []
_sum_ = 0
GAP = []
maxLIST = 0
difference = 0
if _line_ != _column_ or (_line_ <= 0 or _column_ <= 0):
    print("erro")
else:
    
    for l in range(_line_): # lendo os valores
        for c in range(_column_):
            _elements_ = int(input())
            _matrizNum_.append(_elements_)
        _mainList_.append(_matrizNum_)
        _matrizNum_ = []
        
        
    for i in range(_line_): # Maior valor de cada linha
        maxNum = max(_mainList_[i])
        _max_line.append(maxNum)
        if len(_max_line) == _line_:
            print(_max_line)
            maxNum = 0
            for x in range(len(_max_line)):
                if x == 0:
                    maxLIST = _max_line[x]
                elif _max_line[x] > maxLIST: # Maior valor da Matriz
                    maxLIST = _max_line[x]
                    
                    
    for l in range (_line_): # Maior valor de cada coluna
        for c in range(_column_):
            if c == 0:
                maxNum = _mainList_[c][l]
            elif _mainList_[c][l] > maxNum:
                maxNum = _mainList_[c][l]
        _max_column.append(maxNum)
        maxNum = 0
        if len(_max_column) == _column_:
            print(_max_column)
            
            
    for i in range(len(_mainList_)): # Soma dos valores positivos da diagonal
        if _mainList_[i][i] >= 0:
            _sum_ += _mainList_[i][i]
            
            
    count = len(_mainList_)       
    for j in range(len(_mainList_)): # Pegando valores da Diagonal secundaria
        count-=1
        GAP.append(_mainList_[j][count])
        
                   
    for index in range(len(GAP)): # Calculando Diagonal secundaria
        if index == 0:
            difference = GAP[index]
        else:
            difference -= GAP[index]
            
            
    print(maxLIST)
    print(_sum_)
    print(difference)
            
            