# User Settings Manager

User Settings Manager is a simple way to manage user settings using a dictionary. It allows adding, updating, deleting, and viewing settings in a case-insensitive way.

## Features

1. **Add a Setting**
   - Function: `add_setting(dictionary, (key, value))`
   - Converts key and value to lowercase.
   - Prevents duplicate keys (case-insensitive).
   - Returns a success or error message.

2. **Update a Setting**
   - Function: `update_setting(dictionary, (key, value))`
   - Converts key and value to lowercase.
   - Updates an existing setting.
   - Returns a success message if updated or an error if the key does not exist.

3. **Delete a Setting**
   - Function: `delete_setting(dictionary, key)`
   - Converts the key to lowercase.
   - Deletes the key-value pair if it exists.
   - Returns a success message or "Setting not found!" if the key does not exist.

4. **View Settings**
   - Function: `view_settings(dictionary)`
   - Returns `"No settings available."` if the dictionary is empty.
   - Returns a formatted string of all key-value pairs with capitalized keys, each on a new line.


## Example

Input:

```
# Initialize an empty dictionary
settings = {}

# Add settings
print(add_setting(settings, ("Theme", "Dark")))
print(add_setting(settings, ("Volume", "High")))

# Update a setting
print(update_setting(settings, ("Volume", "Medium")))

# View current settings
print(view_settings(settings))

# Delete a setting
print(delete_setting(settings, "Theme"))

# View settings after deletion
print(view_settings(settings))
```

Expected Output:

```
# Add settings
Setting 'theme' added with value 'dark' successfully!
Setting 'volume' added with value 'high' successfully!

# Update a setting
Setting 'volume' updated to 'medium' successfully!

# View current settings
Current User Settings:
Theme: dark
Volume: medium

# Delete a setting
Setting 'theme' deleted successfully!

# View settings after deletion
Current User Settings:
Volume: medium
```

Notes

- All keys and values are handled in a case-insensitive manner.

- The view_settings function formats keys to have their first letter capitalized.

- Duplicate keys cannot be added.