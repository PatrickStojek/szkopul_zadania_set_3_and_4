hexadecimal_number = input()
first_digit = int(hexadecimal_number[0])
second_digit = ord(hexadecimal_number[1])
ascii_code = int(hexadecimal_number[0]) * 16
if second_digit >= ord('A'):
    ascii_code += second_digit - ord('A') + 10
else:
    ascii_code += second_digit - ord('0')

print(ascii_code)
print(chr(ascii_code))
