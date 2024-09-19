def give_bmi(height: list[int | float], weight:
             list[int | float]) -> list[int | float]:
    """Calculate the Body Mass Index"""
    i = 0
    ret = []
    try:
        isinstance(height, list) and is_list_of_numbers(height) \
            and isinstance(weight, list) and is_list_of_numbers(weight)
        len(height) == len(weight)
        for w in weight:
            ret.append(w / (height[i] ** 2))
            i += 1
    except Exception as e:
        raise AssertionError(f"Error: {e}")
    return ret


def is_list_of_numbers(lst: list[int | float]) -> bool:
    """Return True if all elements of the iterable are true
    (or if the iterable is empty)"""
    # all(iterable)
    # Equivalent to:

    # def all(iterable):
    #    for element in iterable:
    #        if not element:
    #            return False
    #    return True

    return all(isinstance(item, int) | isinstance(item, float) for item in lst)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return true if above limit"""
    ret = []
    try:
        isinstance(bmi, list) and is_list_of_numbers(bmi) and \
            isinstance(limit, int)
        for b in bmi:
            if b > limit:
                ret.append(True)
            else:
                ret.append(False)
    except Exception as e:
        raise AssertionError(f"Error: {e}")
    return ret
