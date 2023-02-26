# Print all chars from ASCII table
# in range 33-128
def print_all_chars():
    for c in range(33, 128):
        print(c, "\t", chr(c))


def find_char_id(char):
    return ord(char)


def find_char(char_id):
    return chr(char_id)


# print(find_char_id('!'))
# print(find_char(33))

# Create word from ASCII decimal codes
def create_word(decimal_array):
    res = []
    for i in decimal_array:
        c = find_char(i)
        res.append(c)
    return res


# Create decimal codes from word
def create_decimal(word):
    res = []
    for i in word:
        c = find_char_id(i)
        res.append(c)
    return res


# Convert char array to string
def array_to_string(arr):
    return ''.join(arr)
