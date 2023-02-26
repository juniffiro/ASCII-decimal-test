from src.ascii import *

# Print all table
print_all_chars()

# Create word and print with string format
print(array_to_string(create_word([83, 85, 77, 77, 69, 82])))

# Create ASCII decimal codes from word
print(create_decimal(['S', 'U', 'M', 'M', 'E', 'R']))
print(create_decimal("SUMMER"))
