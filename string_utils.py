def split_at_first_digit(formula: str):
    for i, ch in enumerate(formula):
        if ch.isdigit():
            return formula[:i], int(formula[i:])
    return formula, 1

def split_before_each_uppercases(formula: str):
    """
      "NaCl"     -> ["Na", "Cl"]
      "C6H12O6B" -> ["C6", "H12", "O6", "B"]
      "water"    -> ["water"]
      ""         -> []
    """
    if formula == "": # in case the list is empty, to avoid crash
        return []

    parts = [] 
    current_sum = ""

    for ch in formula: #run on all string by chars and check upper or lower
        if ch.isupper(): #if the current 'ch' is upper, we need to add the last sum
            if current_sum: #not empty
                parts.append(current_sum) # add the sum of ch's that we found till now
            current_sum = ch # start new sum with the new upper 'ch'
        else:
            current_sum += ch # in case the 'ch' still lower

    if current_sum: # we end the loop and still has
        parts.append(current_sum)
    return parts
