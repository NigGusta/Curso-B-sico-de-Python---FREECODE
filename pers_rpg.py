
full_dot = '●'
empty_dot = '○'
def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
       return 'The character name should be a string'
    if len(name) > 10:
       return 'The character name is too long'
    if " " in name:
       return 'The character name should not contain spaces'
    if not all(isinstance(x, int) for x in (strength, intelligence, charisma)):
       return 'All stats should be integers'
    if strength < 1 or intelligence < 1 or charisma < 1:
       return 'All stats should be no less than 1'
    if strength > 4 or intelligence > 4 or charisma > 4:
       return 'All stats should be no more than 4'
    if strength + intelligence + charisma != 7:
       return 'The character should start with 7 points'
    strength_full = full_dot * strength
    strength_empty = (10-strength) * empty_dot
    intelligence_full = full_dot * intelligence
    intelligence_empty = (10-intelligence) * empty_dot
    charisma_full = full_dot * charisma
    charisma_empty = (10-charisma)* empty_dot
    return (
        f"{name}\n"
        f"STR {strength_full}{strength_empty}\n"
        f"INT {intelligence_full}{intelligence_empty}\n"
        f"CHA {charisma_full}{charisma_empty}"
    )
print(create_character("ren", 4, 2, 1))
