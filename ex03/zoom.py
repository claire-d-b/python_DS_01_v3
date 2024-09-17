from load_image import ft_load, slice_me_3d, create_image, print_fig, gray_convert
import matplotlib.pyplot as plt
import numpy as np

def main():
    narray = ft_load("../animal.jpeg")

    img = create_image(narray)
    print(narray)
    width, height = img.size
    sliced_array = slice_me_3d(narray, height-650, height-250, width-600, width-200)
    
    color_image = create_image(sliced_array)

    # # Convert the image to grayscale and create array from black&white image
    # image = color_image.convert('L')

    # gray_array = np.array(image)

    # lst = gray_array.tolist()
    # nlst = []
    # for x, item in enumerate(lst):
    #     nlst.insert(x, [])
    #     for y, unit in enumerate(item):
    #         nlst[x].insert(y, [unit])

    # narray = np.array(nlst)
    gray_array, nlst, image = gray_convert(color_image)
    print(f"New shape after slicing: {tuple((gray_array.shape[0], gray_array.shape[1], 3 - gray_array.ndim))} or {gray_array.shape}")

    print(nlst)

    print_fig(image, 'output.jpeg')

if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")

