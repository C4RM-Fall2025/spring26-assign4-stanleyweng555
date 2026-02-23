
def getBondDuration(y, face, couponRate, m, ppy=1):
    coupon = face * couponRate / ppy
    price = 0
    weighted = 0
    for t in range(1, m * ppy + 1):
        cf = coupon if t < m * ppy else coupon + face
        pvcf = cf / (1 + y/ppy) ** t
        price += pvcf
        weighted += (t / ppy) * pvcf
    return round(weighted / price, 2)
