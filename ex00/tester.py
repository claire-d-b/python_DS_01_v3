from give_bmi import give_bmi, apply_limit


def main():
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    wrongweight = [170, 68.2, 67]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))
    # print(apply_limit(26, bmi))
    # print(apply_limit(0, 0))
    # print(apply_limit(bmi, 0))
    # print(apply_limit(bmi, False))
    wrong_bmi = give_bmi(height, wrongweight)
    print(wrong_bmi)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
