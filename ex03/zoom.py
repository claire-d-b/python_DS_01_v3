from load_image import ft_load


def main():
    # ft_load("../animal.jpeg")
    print(ft_load("../animal.jpeg"))


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
