def solution(n, numlist):
    
    array=[]
    for i in numlist:
        if i%n ==0:
            array.append(i)
    
    return array