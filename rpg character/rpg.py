import sys
sys.stdout.reconfigure(encoding='utf-8')


full_dot = '●'
empty_dot = '○'
max_point = 10

def create_character(char_name, strength, intelligence, charisma):
    if not isinstance(char_name,str):
        return "The character name should be a string"
    if len(char_name) > 10:
        return "The character name is too long"
    if " " in char_name:
        return "The character name should not contain spaces"
    if not isinstance(strength,int) or not isinstance(intelligence,int) or not isinstance(charisma,int):
        return "All stats should be integers"
    if strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"
    if strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"
    if strength + intelligence + charisma != 7:
        return "The character should start with 7 points"

    str_bar = full_dot * strength + empty_dot * (max_point - strength)
    int_bar = full_dot * intelligence + empty_dot * (max_point - intelligence)
    cha_bar = full_dot * charisma + empty_dot * (max_point - charisma)

    return f"{char_name}\nSTR {str_bar}\nINT {int_bar}\nCHA {cha_bar}"