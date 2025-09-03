#!/usr/bin/python3
for dizaine in range(9):
    for unité in range(dizaine + 1, 10):
        if dizaine == 8 and unité == 9:
            print(f"{dizaine}{unité}")
        else:
            print(f"{dizaine}{unité}, ", end="")
