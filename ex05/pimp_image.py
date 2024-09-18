from load_image import ft_invert, ft_red, ft_blue, ft_green, ft_grey, ft_load


def main():
    array = ft_load("../landscape.jpg")
    ft_invert(array)
    ft_red(array)
    ft_green(array)
    ft_blue(array)
    ft_grey(array)
    print(ft_invert.__doc__)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")

