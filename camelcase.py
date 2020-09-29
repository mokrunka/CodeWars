def to_camel_case(text):
    if len(text) == 0:
        return ''
    elif text[0].isupper():
        text = text.title()
        text = text.replace('-','')
        text = text.replace('_', '')
        return text
    elif text[0].islower():
        a = text[0]
        text = text.title()
        text = text.replace('-', '')
        text = text.replace('_', '')
        text= text.replace(text[0], text[0].lower())
        return text

#
to_camel_case('')
to_camel_case("the_stealth_warrior")
to_camel_case("The-Stealth-Warrior")
to_camel_case("A-B-C")

