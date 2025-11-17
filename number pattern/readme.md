# Number Pattern Generator

Number Pattern Generator is a small Python function that creates a string of consecutive integers starting from 1 up to a given number n.
Each number is separated by a space.

## How It Works

The function number_pattern(n):

1. Validates the input:

    - Checks if n is an integer

    - Ensures n is greater than 0

2. Builds the pattern:

    - Loops from 1 to n

    - Adds each number to a string with a space

3. Returns the final string:

    - Removes any trailing spaces before returning

## Example Usage

### Valid inputs

1. print(number_pattern(4))

    Output:  
        ```"1 2 3 4"```

2. print(number_pattern(10))

    Output:  
        ```"1 2 3 4 5 6 7 8 9 10"```

### Invalid inputs

1. print(number_pattern("4"))

    Output:  
        ```"Argument must be an integer value."```

2. print(number_pattern(0))       

    Output:  
        ```"Argument must be an integer greater than 0."```

