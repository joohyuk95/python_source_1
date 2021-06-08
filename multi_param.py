def adding(*val):
    result = 0
    for value in val:
        result += value
    
    print("result = %d" %result)

adding(1, 2, 3, 4)