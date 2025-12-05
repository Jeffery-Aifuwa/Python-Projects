# ISBN Validator

A Python program that validates ISBN-10 and ISBN-13 codes with proper input checks.

## Features

- Accepts ISBN and length as comma-separated input (e.g., `1530051126,10`)
- Validates that the length is numeric
- Checks for invalid characters in ISBNs
  - For ISBN-10, the last character can be a number or `'X'`
  - For ISBN-13, all characters must be digits
- Validates ISBN length (10 or 13 digits) and prints clear error messages
- Calculates the check digit and verifies whether the ISBN is valid
- Prints clear messages for valid or invalid ISBNs

Examples

```
    Enter ISBN and length: 1530051126,10
    Valid ISBN Code.

    Enter ISBN and length: 9781530051120,13
    Valid ISBN Code.

    Enter ISBN and length: 1530051125,10
    Invalid ISBN Code.

    Enter ISBN and length: 080442957X,10
    Valid ISBN Code.
```

## How to Use

1. Run the program:

    `python isbn_validator.py`

2. Enter the ISBN and length separated by a comma:

    `Enter ISBN and length: 1530051126,10`

3. The program will print one of the following messages depending on the input:

    - Valid ISBN Code.

    - Invalid ISBN Code.

    - Invalid character was found.

    - Enter comma-separated values.

    - Length must be a number.

    - ISBN-10 code should be 10 digits long.

    - ISBN-13 code should be 13 digits long.

    - Length should be 10 or 13.


### This project demonstrates:

- Debugging and understanding existing Python code

- Handling input validation and edge cases

- Working with string slicing and list comprehensions

- Implementing ISBN-10 and ISBN-13 check digit calculations