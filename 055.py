move = []
def hanoi (a, b, c, d):
    if a == 1:
        move.append([b,c])
        return None
    