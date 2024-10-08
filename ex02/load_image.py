from PIL import Image
import numpy as np
from array import array


def load_image(image) -> array:
    """Create array from  pillow image"""
    barray = []
    try:
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
    except Exception as e:
        raise AssertionError(f"Error: {e}")
    return np.array(barray)


def ft_load(path: str) -> array:
    """Return an array from image"""
    try:
        Image.open(path)
        image = Image.open(path)
    except Exception:
        raise AssertionError("Error: failed to open file")
    return load_image(image)
