# RPG Character Generator

A simple Python program that creates a character sheet for an RPG adventure.  
The program validates user input and visually displays the character's stats.

---

## 🚀 Features

- **Name Validation**
  - Must be a string
  - Cannot be empty
  - Maximum length: 10 characters
  - No spaces allowed

- **Stat Validation**
  - Must be integers
  - Minimum: 1
  - Maximum: 10
  - (Optional: total points check commented out in current version)

- **Visual Stat Representation**
  - ● = filled stat points
  - ○ = empty points (to reach 10 dots per stat)
    
---

## 🧠 Example Usage

```python
print(create_character("Jotaro", 10, 9, 8))
