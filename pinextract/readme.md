# Pin Extractor

Pin Extractor is a small Python program that generates a numeric “pin” or secret code from a collection of poems.
Each poem is processed line by line, and the code is built by counting the number of letters in specific words according to their line positions.

## How It Works

- Split the text into lines using \n.

- Loop through each line and get all the words.

- If the number of words in the line is greater than the line’s index,
add the length of the word at that same index to the code.
Otherwise, add '0'.

- After processing all lines, append the generated code to a list of secret codes.

## Example

Input:
``` 
poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = """The grass is green
here and there
hoping for rain
before it turns yellow"""

poem3 = """Whispers drift across the sea  
Dreams awaken silently  
Stars align where hearts belong  
Night hums its eternal song  
"""

print(pin_extractor([poem, poem2, poem3]))
```

Output:

`['5202', '3346', '86570']`

## How to Run

- Save the file as pin_extractor.py.

- Run the script using: `python pin_extractor.py`

- Modify or add more poems in the list to generate new secret pins.