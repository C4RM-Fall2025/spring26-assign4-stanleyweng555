
def getBondPrice_Z(face, couponRate, times, yc):
    cash_flows = [face * couponRate] * len(times)
    cash_flows[-1] += face
    price = sum(cf / (1 + r) ** t for cf, r, t in zip(cash_flows, yc, times))
    return round(price)
