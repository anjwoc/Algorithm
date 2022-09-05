def get_distance(x1, y1, x2, y2):
    return int(((x2-x1)**2 + (y2-y1)**2) ** 0.5)


print(get_distance(0, 0, 3, 2))
