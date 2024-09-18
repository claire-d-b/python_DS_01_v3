from load_image import ft_load


def main():
    print(ft_load("../landscape.jpg"))
    print(ft_load("landscape.jpg"))
    print(ft_load(0))
    print(ft_load(""))


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
