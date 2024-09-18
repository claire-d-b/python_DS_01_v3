from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import array

# Grayscale ('L' Mode):
# Channels: 1 (Intensity)
# Description: Each pixel value represents the intensity of the grayscale color, ranging from black (0) to white (255). There is no alpha channel in this mode.
# To create a grayscale image from a 3D list using Pillow, you need to ensure that the 3D list represents an image where the third dimension contains only one value (the grayscale intensity). The 3D list should be structured as [height][width][1], where each sub-list represents a row of pixels, and each pixel has a single grayscale intensity value.

def slice_me_3d(family: list, start_x: int, end_x: int, start_y: int, end_y: int) -> list:
    ret = []
    if isinstance(family, list):
        ret = family[start_x:end_x]
        for x, row in enumerate(ret):
            ret[x] = row[start_y:end_y]
    else:
        raise AssertionError("Error: parameter is not a list")
    return ret

def create_image(barray: list) -> Image:
    """Create image from array"""
    # Get the dimensions of the image
    height = len(barray)
    width = len(barray[0])

    # Create a new Pillow image with RGB mode
    image = Image.new('RGB', (width, height))

    # Populate the image with pixel values
    pixels = image.load()
    for y, row in enumerate(barray):
        for x, color in enumerate(row):
            pixels[x, y] = tuple(color)

    # Save the image as a JPEG file
    return image

def gray_convert(color_image: Image) -> tuple:
    """Convert the image to grayscale and create array from black&white image"""
    image = color_image.convert('L')

    gray_array = np.array(image)

    lst = gray_array.tolist()
    nlst = []
    for x, item in enumerate(lst):
        nlst.insert(x, [])
        for y, unit in enumerate(item):
            nlst[x].insert(y, [unit])

    return tuple((gray_array, nlst, image))

def print_fig(image: Image, name: str) -> None:
    """Save data as a figure"""
    # Convert the Pillow image to a NumPy array
    data_np = np.array(image)

    # Step 3: Display the Image in a Matplotlib Figure
    fig, ax = plt.subplots()

    # Display the data as an image
    img_ax = ax.imshow(data_np, cmap='gray')

    # Save the figure (optional)
    fig.savefig(name, format='JPEG')

def rotate(three_d_lst: list) -> list:
    # Rotate the 3D list 90° to the left
    # When -1 is used as the step, it means to iterate in reverse order.
    # stopping before -1. The -1 step indicates to count backwards.

    rotated_list = []
    for i in range(len(three_d_lst[0]) - 1, -1, -1):
        rotated_list.insert(len(three_d_lst[0]) - 1 - i, [])
        for j in range(0, len(three_d_lst)):
            rotated_list[len(three_d_lst[0]) -1 - i].insert(j, three_d_lst[j][i])

    # <=> list comprehension: rotated_list = [[three_d_lst[j][i] for j in range(len(three_d_lst))] for i in range(len(three_d_lst[0]) - 1, -1, -1)]

    return rotated_list

def ft_load(path: str) -> array:
    try:
        Image.open(path)
        image = Image.open(path)
        barray = []

        width, height = image.size

        for x in range(height):
            barray.insert(x, [])
            for y in range(width):
                r, g, b = image.getpixel((y, x))
                barray[x].insert(y, [r, g, b])
        
        string = "The shape of image is: "
        items = image.getpixel((0, 0))
        i = 0
        for item in items:
            i += 1
        print(string, (height, width, i))

        sliced_array = slice_me_3d(barray, height-650, height-250, width-600, width-200)
        nbarray = rotate(sliced_array)
        color_image = create_image(nbarray)
        gray_array, nlst, image = gray_convert(color_image)
        print_fig(image, 'output.jpeg')

    except AssertionError as e:
        raise AssertionError("Error: failed to open file")
    return nbarray