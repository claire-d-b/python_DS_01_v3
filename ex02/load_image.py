from PIL import Image
import array

def load_image(image) -> array:
    try:
        barray = [[]]

        width, height = image.size

        for x in range(0, height):
            for y in range(0, width):
                r, g, b = image.getpixel((y, x))
                barray[0].append([r, g, b])

        string = "The shape of image is: "
        items = image.getpixel((0, 0))
        i = 0
        for item in items:
            i += 1
        print(string, (height, width, i))
    except e:
        raise AssertionError(e)
    return barray

def ft_load(path: str) -> array:
    try:
        Image.open(path)
        image = Image.open(path)
        return load_image(image)
    except AssertionError as e:
        raise AssertionError("Error: failed to open file")
