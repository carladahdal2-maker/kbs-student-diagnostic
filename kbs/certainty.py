def cf_combine(cf1: float, cf2: float) -> float:
    """دمج دليلين حسب قواعد MYCIN (موجب/موجب، سالب/سالب، مختلفان)."""
    if cf1 >= 0 and cf2 >= 0:
        return cf1 + cf2 * (1 - cf1)
    if cf1 < 0 and cf2 < 0:
        return cf1 + cf2 * (1 + cf1)
    denom = 1 - min(abs(cf1), abs(cf2))
    return (cf1 + cf2) / denom if denom != 0 else (cf1 + cf2)
