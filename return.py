def return_tuple(start, end):
    even_sum, odd_sum = 0, 0
    for num in range(start, end+1):
        if num % 2:
            odd_sum += num
        else:
            even_sum += num
    
    return even_sum, odd_sum

start = int(input("시작값 : "))
end = int(input("끝값 : "))

even_sum = return_tuple(start, end)[0]
odd_sum = return_tuple(start, end)[1]

print("{}부터 {}까지의 짝수합은 {}, 홀수합은 {}".format(start, end, even_sum, odd_sum))