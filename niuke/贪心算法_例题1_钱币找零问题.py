def greedy1():       
    #面额
    values = { 1, 2, 5, 10, 20, 50, 100 };
    #数量
    counts = { 3, 3, 2, 1, 1, 3, 3 };
    #获取需要各种面值多少张
    result = getNumber1(446, values, counts);             

def getNumber1(sum , values, counts):
	
    result = [0 for i in range(len(values))];
    add=0; #当前凑的金额
    for i in range(len(result), 1, -1):
        num = (sum-add)/values[i];
        if num>counts[i]:
            num=counts[i];
        add=add+num*values[i];
        result[i]=num;
    
    return result;		
	
