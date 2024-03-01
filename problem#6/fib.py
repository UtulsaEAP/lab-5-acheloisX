def fibonacci(n):
    a = 0
    b = 1
    c = 1
    
    if (n < 0):
        return -1
    
    
    for i in range(1,n):
        
        c = a + b
        a = b
        b = c
    
    return c 

if __name__ == '__main__':
    start_num = int
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')