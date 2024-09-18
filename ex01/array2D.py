def slice_me(family: list, start: int, end: int) -> list:
    """Slice a two dimensional array"""
    ret = []
    try:
        assert isinstance(family, list) and isinstance(start, int) and \
            isinstance(end, int), "Error: wrong type for parameters"
        rows = len(family[0])
        ret = family[start:end]
        for f in family:
            assert rows == len(f), "Error: inner lists are not the same size"

        shape = (len(family), len(family[0]))
        nshape = (len(ret), len(ret[0]))
        print("My shape is: ", shape)
        print("My new shape is: ", nshape)

    except AssertionError as e:
        print(f"AssertionError: {e}")

    return ret
