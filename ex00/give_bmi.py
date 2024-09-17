
def give_bmi(height: list[int | float], weight:
             list[int | float]) -> list[int | float]:
    i = 0
    ret = []
    try:
        len(height) == len(weight)
        for w in weight:
            ret.append(w / (height[i] ** 2))
            i += 1
    except AssertionError as e:
        raise AssertionError("Error: length of the lists differ")
    return ret


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    ret = []
    for b in bmi:
        try:
            str(type(b))[8:2] == 'float' or str(type(b))[8:2] == 'int'
            if b > limit:
                ret.append(True)
            else:
                ret.append(False)
        except AssertionError as e:
            raise AssertionError("Error: types is neither int nor float")
    return ret