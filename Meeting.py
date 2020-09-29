def meeting(s):
    reversed = []
    result = []
    # fix punctuation and capitalization
    s = s.split(';')
    for name in s:
        name = name.upper()
        result.append(name.replace(':', ', '))
    # reverse order of fname/lname
    for name in result:
        name = name.split(',')
        reversed.append(name)

    for name in reversed:
        lname = name[1]
        fname = name[0]
        name[0] = lname
        name[1] = fname

    result = []
    result_string = ''
    reversed.sort()
    for name in reversed:
        result_string += f'({name[0].strip()}, {name[1]})'

    return result_string


meeting("Alexis:Wahl;John:Bell;Victoria:Schwarz;Abba:Dorny;Grace:Meta;Ann:Arno;Madison:STAN;Alex:Cornwell;Lewis:Kern;Megan:Stan;Alex:Korn")