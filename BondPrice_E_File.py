
def getBondPrice_E(face, couponRate, yc):
    cash_flows = [face * couponRate] * len(yc)
    cash_flows[-1] += face
    price = 0
    for t, cf in enumerate(cash_flows, start=1):
        price += cf / (1 + yc[t-1]) ** t
    return round(price)
