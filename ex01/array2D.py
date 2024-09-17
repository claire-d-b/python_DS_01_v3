def slice_me(family: list, start: int, end: int) -> list:
    ret = []
    if isinstance(family, list):
        lencol = len(family[0])
        ret = family[start:end]
        for f in family:
            if lencol != len(f):
                raise AssertionError("Error: inner lists are not the same size")
                return None
        shape = (len(family), len(family[0]))
        nshape = (len(ret), len(ret[0]))
        print("My shape is: ", shape)
        print("My new shape is: ", nshape)

    else:
        raise AssertionError("Error: parameter is not a list")
        return None
    return ret
