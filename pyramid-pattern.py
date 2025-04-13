# Number of rows in the pyramid
rows = 5

# Loop from 1 to rows (inclusive)
for i in range(1, rows + 1):
    # Calculate number of spaces needed before stars
    # As i increases, we need fewer spaces
    spaces = ' ' * (rows - i)
    
    # Calculate number of stars for current row
    # Formula: 2*i - 1 gives odd numbers (1,3,5,7,9) for increasing i
    stars = '*' * (2 * i - 1)
    
    # Print the spaces followed by stars for current row
    print(spaces + stars)
  
