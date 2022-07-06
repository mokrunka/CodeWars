def calculator(txt):
    arg_list = txt.split()
    first_dots = len(arg_list[0])
    second_dots = len(arg_list[2])
    if arg_list[1] == '+':
        return (first_dots + second_dots) * '.'
    elif arg_list[1] == '-':
        return (first_dots - second_dots) * '.'
    elif arg_list[1] == '*':
        return (first_dots * second_dots) * '.'
    elif arg_list[1] == '//':
        return (first_dots // second_dots) * '.'

calc("..... + ...............")
calc("..... - ...")
calc("..... - .")
calc("..... * ...")
calc("..... * ..")
calc("..... // ..")
calc("..... // .")
calc(". // ..")
calc(". - .")
