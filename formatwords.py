def format_words(words):
    result_string = ''
    i = 0
    if words == None:
        return result_string
    while '' in words:
        words.remove('')
    if len(words) == 1:
        result_string += words[0]
        return result_string
    elif len(words) == 0:
        return result_string
    while i < len(words) - 1:
        result_string += words[i] + ', '
        i += 1
    result_string = result_string[:-2]
    result_string += ' and ' + words[-1]
    return (result_string)

# format_words(['one', 'two', 'three', 'four'])
# format_words(['one'])
# format_words(['one', '', 'three'])
format_words(['', '', 'three'])