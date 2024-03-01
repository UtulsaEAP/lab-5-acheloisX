def int_to_reverse_binary(integer_val):
    binary_val = ''
    if integer_val == 0:
        return '0'
    while integer_val > 0:
        binary_val += str(integer_val % 2)
        integer_val = integer_val // 2
    return binary_val

def string_reverse(input_string): 
    reverse_input = ''

    for char in input_string[::-1]:
        reverse_input += char
    return reverse_input

if __name__ == '__main__':
    user_input = int(input())
    
    binary_string = int_to_reverse_binary(user_input)
    reversed_binary_string = string_reverse(binary_string)
    
    print(reversed_binary_string)