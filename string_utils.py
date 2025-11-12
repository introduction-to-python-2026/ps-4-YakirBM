def split_before_each_uppercases(formula: str):
    """
    Split the string before every uppercase letter.
    Keep the uppercase letters at the start of each chunk.
    Examples:
      "NaCl"     -> ["Na", "Cl"]
      "C6H12O6"  -> ["C6", "H12", "O6"]
      "abc"      -> ["abc"]
      ""         -> [""]
    """
    if not formula:
        return [""]

    parts = []
    current = ""

    for ch in formula:
        if ch.isupper():
            # אם יש לנו חלק קיים, נסיים אותו ונתחיל חדש עם האות הגדולה
            if current:
                parts.append(current)
            current = ch
        else:
            current += ch

    # הוסף את החלק האחרון
    parts.append(current)
    return parts


def split_at_first_digit(formula: str):
    """
    Split at the first digit:
    - Prefix: substring before the first digit
    - Number: first digit onward, parsed as int
    If no digits exist, return (formula, 1)

    Examples:
      "H22"   -> ("H", 22)
      "NaCl"  -> ("NaCl", 1)
      "123"   -> ("", 123)
      ""      -> ("", 1)
    """
    for i, ch in enumerate(formula):
        if ch.isdigit():
            return formula[:i], int(formula[i:])
    return formula, 1
