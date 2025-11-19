def add_setting(a, b):
    key, value = b
    key = key.lower()
    value = value.lower()
    if key in a.keys(): 
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        a[key] = value 
        return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(c,d):
    key, value = d
    key = key.lower()
    value = value.lower()
    if key in c.keys():
        c[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(e,f):
    key = f
    key = key.lower()
    if key in e.keys():
        e.pop(key)
        return f"Setting '{key}' deleted successfully!"
    else:
        return f"Setting not found!"


def view_settings(g):
    if g == {}:
        return f"No settings available."
    else:
        output = "Current User Settings:\n"
        for key, value in g.items():
            output += f"{key.title()}: {value}\n"
        return output