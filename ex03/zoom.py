from load_image import ft_load, slice_me_3d, create_image, print_fig, gray_convert
import matplotlib.pyplot as plt
import numpy as np

def main():
    narray = ft_load("../animal.jpeg")

if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")

