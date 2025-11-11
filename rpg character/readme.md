# RPG Character

This project is a Python program that allows you to create a simple RPG (Role-Playing Game) character. The program validates character information and visually displays the character’s stats using symbols.

## Features

1. Ensures the character name:

    - Is a string

    - Does not contain spaces

    - Has a maximum length of 10 characters

2. Validates stats (Strength, Intelligence, Charisma):

    -  Must be integers

    -  Must be between 1 and 4

    -  Total points must equal 7

3. Displays a visual bar for each stat using filled (●) and empty (○) symbols

4. Returns a multi-line string showing the character’s name and stats

## Usage

1. Define a character by calling the function:
```
create_character(char_name, strength, intelligence, charisma)
```

- `char_name`: string (max 10 characters, no spaces)

- `strength`, `intelligence`, `charisma`: integers between 1 and 4

 - Total points of all three stats must equal 7

2. Example:
```
print(create_character("Ren", 4, 2, 1))
```

Output:
```
Ren
STR ●●●●○○○○○○
INT ●●○○○○○○○○
CHA ●○○○○○○○○○
```

## How it Works

1. Validation: The function checks the character name and stats for correct types and limits.

2. Bar creation: Each stat is represented as a combination of filled and empty symbols to give a visual representation of the value.

3. Return output: After passing all checks, the function returns a multi-line string with the character name and stats.