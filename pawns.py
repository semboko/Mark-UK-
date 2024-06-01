def safe_pawns(coords: set) -> int:
    counter = 0
    
    for pawn in coords:
        letter, number = pawn
        guard_horizontal = str(int(number) - 1)
        guard_vertical1 = chr(ord(letter) - 1)
        guard_vertical2 = chr(ord(letter) + 1)
        
        guard1 = guard_vertical1 + guard_horizontal
        guard2 = guard_vertical2 + guard_horizontal
        
        if guard1 in coords or guard2 in coords:
            counter = counter + 1
    
    return counter

assert safe_pawns({"d2", "f4", "d4", "b4", "e3", "g5", "c3"}) == 6
assert safe_pawns({"f4", "g4", "d4", "b4", "e4", "e5", "c4"}) == 1
print("Done")