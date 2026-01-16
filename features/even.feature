  # TODO: Írd ide a scenariókat!
  # 1. Páros szám ellenőrzése (pl. 4)
  # 2. Páratlan szám ellenőrzése (pl. 5)
  # 3. Nulla ellenőrzése (0)
  # 4. Negatív páros szám ellenőrzése (-4)
  # 5. Negatív páratlan szám ellenőrzése (-5)


Feature: Is it even/odd?

Scenario Outline: The number is even or odd
  Given the number is "<number>"
  When I ask whether it's even or odd
  Then I should be told "<answer>"

Examples:
  | number | answer |
  | 4 | even |
  | 5 | odd |
  | 0 | even |
  | -4 | even |
  | -5 | odd |


