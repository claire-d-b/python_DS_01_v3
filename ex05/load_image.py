from PIL import Image, ImageOps
import numpy as np
import array


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
    """Convert the image to grayscale and create array from
    black&white image"""
    image = color_image.convert('L')

    gray_array = np.array(image)

    lst = gray_array.tolist()
    nlst = []
    for x, item in enumerate(lst):
        nlst.insert(x, [])
        for y, unit in enumerate(item):
            nlst[x].insert(y, [unit])

    return tuple((gray_array, nlst, image))


def ft_invert(array) -> array:
    """Inverts the color of the image received."""
    output_image_path = "Invert.jpeg"
    barray = []
    try:
        image = create_image(array)

        # Invert the image
        inverted_image = ImageOps.invert(image)

        # Save the inverted image
        inverted_image.save(output_image_path)

        width, height = inverted_image.size

        for x in range(0, height):
            barray.insert(x, [])
            for y in range(0, width):
                r, g, b = inverted_image.getpixel((y, x))
                barray[x].insert(y, [r, g, b])
    except Exception:
        raise AssertionError("Error: failed to create image")

    return barray


def ft_red(array) -> array:
    """Displays bluescale image by setting b and g to 0"""
    output_image_path = "Red.jpeg"
    barray = []
    try:
        nimage = create_image(array)

        width, height = nimage.size

        for x in range(0, height):
            barray.insert(x, [])
            for y in range(0, width):
                r, g, b = nimage.getpixel((y, x))
                barray[x].insert(y, [r, 0, 0])

        red_image = create_image(barray)
        red_image.save(output_image_path)

    except Exception:
        raise AssertionError("Error: failed to create image")

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
                barray[x].insert(y, [0, g, 0])

        green_image = create_image(barray)
        green_image.save(output_image_path)

    except Exception:
        raise AssertionError("Error: failed to create image")

    return barray


def ft_grey(array) -> array:
    """ Grayscale colors are those where the red, green, and blue
        components are all equal.
        The RGB values that make up shades of gray range from (0, 0, 0)
        for black to (255, 255, 255) for white, with intermediate values
        representing different shades of gray. """
    output_image_path = "Grey.jpeg"
    barray = []
    try:
        nimage = create_image(array)
        gray_array, nlst, gray_image = gray_convert(nimage)
        gray_image.save(output_image_path)

        width, height = nimage.size

        for x in range(0, height):
            barray.insert(x, [])
            for y in range(0, width):
                r, g, b = nimage.getpixel((y, x))
                barray[x].insert(y, [r, g, b])

    except Exception:
        raise AssertionError("Error: failed to create image")
    return barray


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
