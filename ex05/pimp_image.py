from load_image import ft_invert, ft_red, ft_blue, ft_green, ft_gray


def main():
    print(ft_invert("../landscape.jpg"))
    print(ft_red("../andscape.jpg"))
    print(ft_blue("../landscape.jpg"))
    print(ft_green("../landscape.jpg"))
    print(ft_gray("../landscape.jpg"))
    print(ft_invert.__doc__)


if __name__ == "__main__":
    main()
