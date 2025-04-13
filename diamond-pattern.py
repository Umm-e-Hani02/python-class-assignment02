# Number of rows for the upper half of the diamond
rows = 5

# Upper half of the diamond
for i in range(1, rows + 1):
    # Calculate number of spaces before stars (decreases as i increases)
    spaces = ' ' * (rows - i)
    # Calculate number of stars (increases by 2 for each row)
    stars = '*' * (2 * i - 1)
    # Print the spaces followed by stars for this row
    print(spaces + stars)

# Lower half of the diamond (excluding the middle row)
for i in range(4, 0, -1):
    # Calculate number of spaces before stars (increases as i decreases)
    spaces = ' ' * (rows - i)
    # Calculate number of stars (decreases by 2 for each row)
    stars = '*' * (2 * i - 1)
    # Print the spaces followed by stars for this row
    print(spaces + stars)