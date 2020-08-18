class HTML:
    def __init__(self, string):
        self.string = string
        self.div = '<div>' + string + '</div>'
        self.p = '<p>' + string + '</p>'

class Format(HTML):
    def __init__(self, string):
        super().__init__(string)
        pass

a_string = Format('a test string')

print(type(a_string.div))
print(a_string.string)
print(a_string.div)
print(a_string.p)
print(a_string.div)