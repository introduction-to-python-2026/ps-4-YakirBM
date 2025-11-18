def split_before_each_uppercases(formula: str):
    """
      "NaCl"     -> ["Na", "Cl"]
      "C6H12O6B" -> ["C6", "H12", "O6", "B"]
      "water"    -> ["water"]
      ""         -> []
    """
    if formula == "":
        return []

    parts = []
    current_sum = ""

    for ch in formula: #run on all string by chars and check upper or lower
        if ch.isupper(): #if the 
            if current_sum: #not empty
                parts.append(current_sum)
            current_sum = ch
        else:
            current_sum += ch

    if current_sum:
        parts.append(current_sum)
    return parts


def split_at_first_digit(formula: str):
    for i, ch in enumerate(formula):
        if ch.isdigit():
            return formula[:i], int(formula[i:])
    return formula, 1
