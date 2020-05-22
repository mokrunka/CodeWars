def encode(st):
    decoder_ring = ('aeiou', '12345')
    decoder_table = st.maketrans(decoder_ring[0], decoder_ring[1])
    return st.translate(decoder_table)

def decode(st):
    decoder_ring = ('aeiou', '12345')
    decoder_table = st.maketrans(decoder_ring[1], decoder_ring[0])
    return st.translate(decoder_table)

encode('This is an encoding test.')
decode('h2ll4')