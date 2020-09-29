def rgb(r, g, b):
    hex_code_map = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    hex_code = ''

    if r < 0:
        r = 0
    if g < 0:
        g = 0
    if b < 0:
        b = 0
    if r > 255:
        r = 255
    if g > 255:
        g = 255
    if b > 255:
        b = 255

    if r % 16 == 0:
        hex_code += hex_code_map[r // 16] + '0'
    else:
        quotient = r // 16
        remainder = abs(quotient - (r / 16))
        hex_code += hex_code_map[int(quotient)] + hex_code_map[int(remainder * 16)]

    if g % 16 == 0:
        hex_code += hex_code_map[g // 16] + '0'
    else:
        quotient = g // 16
        remainder = abs(quotient - (g / 16))
        hex_code += hex_code_map[int(quotient)] + hex_code_map[int(remainder * 16)]

    if b % 16 == 0:
        hex_code += hex_code_map[b // 16] + '0'
    else:
        quotient = b // 16
        remainder = abs(quotient - (b / 16))
        hex_code += hex_code_map[int(quotient)] + hex_code_map[int(remainder * 16)]

    return (hex_code)

# rgb(0,0,0)
# rgb(1,2,3)
# rgb(255,255,255)
# rgb(254,253,252)
rgb(-20,275,125)