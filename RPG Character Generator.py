def create_character(name, strength, intelligence, charisma):
    # Validate name 
    if not isinstance(name, str):
        return "The character name should be a string"
    if name == "":
        return "The character should have a name"
    if len(name) > 10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"
    
    # Validate stats type
    if not all(isinstance(stat, int) for stat in [strength, intelligence, charisma]):
        return "All stats should be integers"
    
    # Validate stat ranges
    if any(stat < 1 for stat in [strength, intelligence, charisma]):
        return "All stats should be no less than 1"
    if any(stat > 10 for stat in [strength, intelligence, charisma]):
        return "All stats should be no more than 10"
    
      # Validate total points
    '''
    if (strength + intelligence + charisma) != 30:
        return "The character should start with 30 points"
    '''
  
    
    # Helper function to create stat line
    def stat_line(label, value):
        return f"{label} {'●' * value}{'○' * (10 - value)}"
    
    # Build output
    result = "\n".join([
        name,
        stat_line("STR", strength),
        stat_line("INT", intelligence),
        stat_line("CHA", charisma)
    ])
    
    return result

# Example usage
print(create_character("Jotaro", 10, 9, 8))

