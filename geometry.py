def orientation(p, q, r):
    Xp, Yp = p
    Xq, Yq = q
    Xr, Yr = r
    # Return -1 = ccw
    # Return  1 = cw
    # Return  0 = collinear
    value = (Yq - Yp) * (Xr - Xq) - (Yr - Yq) * (Xq - Xp)
    if value < 0:
        return -1
    if value > 0:
        return 1
    return 0


def do_intersect(p1, q1, p2, q2):
    return (orientation(p1, q1, p2) != orientation(p1, q1, q2) 
            and 
            orientation(p2, q2, p1) != orientation(p2, q2, q1))