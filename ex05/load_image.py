from PIL import Image
import numpy as np
from array import array


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


def ft_invert(array) -> array:
    """Inverts the color of the image received."""
    output_image_path = "Invert.jpeg"
    barray = []
    try:
        nimage = create_image(array)

        width, height = nimage.size

        for x in range(0, height):
            barray.insert(x, [])
            for y in range(0, width):
                r, g, b = nimage.getpixel((y, x))
                barray[x].insert(y, [(r - 255) * -1,
                                     (g - 255) * -1,
                                     (b - 255) * -1])

        invert_image = create_image(barray)
        invert_image.save(output_image_path)

    except Exception:
        raise AssertionError("Error: failed to create image")

    return barray


def ft_red(array) -> array:
    """Displays bluescale image by setting b and g to 0"""
    output_image_path = "Red.jpeg"
    barray = []
    try:
        nimage = create_image(array)
        nimage.save(output_image_path)

        width, height = nimage.size

        for x in range(0, height):
            barray.insert(x, [])
            for y in range(0, width):
                r, g, b = nimage.getpixel((y, x))
                barray[x].insert(y, [r * 1, g * 0, b * 0])

        red_image = create_image(barray)
        red_image.save(output_image_path)

    except Exception as e:
        raise AssertionError(f"Error: {e}")

    return barray


def ft_blue(array) -> array:
    """Displays bluescale image by setting r and g to 0"""
    output_image_path = "Blue.jpeg"
    barray = []
    try:
        nimage = create_image(array)
        nimage.save(output_image_path)

        width, height = nimage.size

        for x in range(0, height):
            barray.insert(x, [])
            for y in range(0, width):
                r, g, b = nimage.getpixel((y, x))
                barray[x].insert(y, [0, 0, b])

        blue_image = create_image(barray)
        blue_image.save(output_image_path)

    except Exception:
        raise AssertionError("Error: failed to create image")

    return barray


def ft_green(array) -> array:
    """Displays bluescale image by setting r and b to 0"""
    output_image_path = "Green.jpeg"
    barray = []
    try:
        nimage = create_image(array)
        nimage.save(output_image_path)

        width, height = nimage.size

        for x in range(0, height):
            barray.insert(x, [])
            for y in range(0, width):
                r, g, b = nimage.getpixel((y, x))
                barray[x].insert(y, [r-r, g, b-b])

        green_image = create_image(barray)
        green_image.save(output_image_path)

    except Exception:
        raise AssertionError("Error: failed to create image")

    return barray


def ft_grey(array) -> array:
    """Convert the image to grayscale and create array from
    black&white image"""
    # Grayscale colors are those where the red, green, and blue
    # components are all equal.
    # The RGB values that make up shades of gray range from (0, 0, 0)
    # for black to (255, 255, 255) for white, with intermediate values
    # representing different shades of gray. """

    output_image_path = "Grey.jpeg"
    color_image = create_image(array)
    barray = []
    try:
        width, height = color_image.size

        for x in range(0, height):
            barray.insert(x, [])
            for y in range(0, width):
                r, g, b = color_image.getpixel((y, x))
                component_value = int(r / 3 + g / 3 + b / 3)
                barray[x].insert(y, [component_value,
                                     component_value, component_value])

        gray_image = create_image(barray)
        gray_image.save(output_image_path)

    except Exception as e:
        raise AssertionError(f"Error: {e}")


def load_image(image) -> array:
    """Create array from  pillow image"""
    try:
        barray = []

        width, height = image.size

        for x in range(0, height):
            barray.insert(x, [])
            for y in range(0, width):
                r, g, b = image.getpixel((y, x))
                barray[x].insert(y, [r, g, b])

        string = "The shape of image is: "
        items = image.getpixel((0, 0))
        i = 0
        for item in items:
            i += 1
        print(string, (height, width, i))
        print(np.array(barray))
    except Exception:
        raise AssertionError("An error occured")
    return np.array(barray)


def ft_load(path: str) -> array:
    """Return an array from image"""
    try:
        Image.open(path)
        image = Image.open(path)
    except Exception:
        raise AssertionError("Error: failed to open file")
    return load_image(image)
