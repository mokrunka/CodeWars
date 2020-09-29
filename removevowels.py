def disemvowel(string):
    ord_list = [97, 101, 105, 111, 117, 65, 69, 73, 79, 85]
    for char in string:
        if ord(char) in ord_list:
            string = string.replace(char, '')
    return string

disemvowel("This website is for losers LOL!")