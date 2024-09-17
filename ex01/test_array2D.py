from array2D import slice_me


def main():
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]
    familywrong = [[1.80, 78.4],
              [2.15],
              [2.10, 98.5],
              [1.88, 75.2]]
    wrongtype = { "a", 2, "c"}
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))
    # print(slice_me(familywrong, 0, 2))
    # print(slice_me(wrongtype, 1, -2))


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")