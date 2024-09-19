def slice_me(family: list, start: int, end: int) -> list:
    """Slice a two dimensional array"""
    ret = []
    try:
        isinstance(family, list) and isinstance(start, int) and \
isinstance(end, int)
        rows = len(family[0])
        ret = family[start:end]
        for f in family:
            if rows != len(f):
                raise AssertionError(f"Length of sublists in main list differ")


        shape = (len(family), len(family[0]))
        nshape = (len(ret), len(ret[0]))
        print("My shape is: ", shape)
        print("My new shape is: ", nshape)

    except Exception as e:
        raise AssertionError(f"Error: {e}")

    return ret
