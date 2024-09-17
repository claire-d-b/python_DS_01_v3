from PIL import Image, ImageOps


def ft_invert(path: str) -> bytearray:
    """Inverts the color of the image received."""
    input_image_path = path
    output_image_path = "pimp_image_inv.jpeg"
    barray = []
    try:
        assert Image.open(input_image_path)
        """ Open the image """
        image = Image.open(input_image_path)

        """ Invert the image """
        inverted_image = ImageOps.invert(image)

        """ Save the inverted image """
        inverted_image.save(output_image_path)

        width, height = image.size

        string = "The shape of image is: "
        items = image.getpixel((0, 0))
        i = 0
        for item in items:
            i += 1
        print(string, (height, width, i))

        for x in range(width):
            for y in range(height):
                r, g, b = image.getpixel((x, y))
                barray.append([r, g, b])
        barray.append([r, g, b])

    except AssertionError as e:
        print(f"AssertionError: {e}")

    return barray


def ft_red(path: str) -> bytearray:
    input_image_path = path
    output_image_path = "pimp_image_red.jpeg"
    barray = []
    try:
        assert Image.open(input_image_path)
        image = Image.open(input_image_path)

        width, height = image.size

        string = "The shape of image is: "
        items = image.getpixel((0, 0))
        i = 0
        for item in items:
            i += 1
        print(string, (height, width, i))

        for x in range(height):
            for y in range(width):
                r, g, b = image.getpixel((y, x))
                barray.extend([r, 0, 0])
        barray.extend([r, 0, 0])

        """ Convert the flat list of RGB values to bytes """
        rgb_bytes = bytes(barray)

        """ Create an RGB image from bytes """
        img = Image.frombytes('RGB', (width, height), rgb_bytes)

        img.save(output_image_path)

    except AssertionError as e:
        print(f"AssertionError: {e}")

    return barray


def ft_blue(path: str) -> bytearray:
    input_image_path = path
    output_image_path = "pimp_image_blue.jpeg"
    barray = []
    try:
        assert Image.open(input_image_path)
        image = Image.open(input_image_path)

        width, height = image.size

        string = "The shape of image is: "
        items = image.getpixel((0, 0))
        i = 0
        for item in items:
            i += 1
        print(string, (height, width, i))

        for x in range(height):
            for y in range(width):
                r, g, b = image.getpixel((y, x))
                barray.extend([0, 0, b])
        barray.extend([0, 0, b])

        """ Convert the flat list of RGB values to bytes """
        rgb_bytes = bytes(barray)

        """ Create an RGB image from bytes """
        img = Image.frombytes('RGB', (width, height), rgb_bytes)

        img.save(output_image_path)

    except AssertionError as e:
        print(f"AssertionError: {e}")

    return barray


def ft_green(path: str) -> bytearray:
    input_image_path = path
    output_image_path = "pimp_image_green.jpeg"
    barray = []
    try:
        assert Image.open(input_image_path)
        image = Image.open(input_image_path)

        width, height = image.size

        string = "The shape of image is: "
        items = image.getpixel((0, 0))
        i = 0
        for item in items:
            i += 1
        print(string, (height, width, i))

        for x in range(height):
            for y in range(width):
                r, g, b = image.getpixel((y, x))
                barray.extend([0, g, 0])
        barray.extend([0, g, 0])

        """ Convert the flat list of RGB values to bytes """
        rgb_bytes = bytes(barray)

        """ Create an RGB image from bytes """
        img = Image.frombytes('RGB', (width, height), rgb_bytes)

        img.save(output_image_path)

    except AssertionError as e:
        print(f"AssertionError: {e}")

    return barray


def ft_gray(path: str) -> bytearray:
    input_image_path = path
    output_image_path = "pimp_image_gray.jpeg"
    barray = []
    try:
        assert Image.open(input_image_path)
        image = Image.open(input_image_path)

        width, height = image.size

        string = "The shape of image is: "
        items = image.getpixel((0, 0))
        i = 0
        for item in items:
            i += 1
        print(string, (height, width, i))

        """ Grayscale colors are those where the red, green, and blue
        components are all equal.
        The RGB values that make up shades of gray range from (0, 0, 0)
        for black to (255, 255, 255) for white, with intermediate values
        representing different shades of gray. """

        for x in range(height):
            for y in range(width):
                r, g, b = image.getpixel((y, x))
                barray.extend([r, r, r])
        barray.extend([r, r, r])

        """ Convert the flat list of RGB values to bytes """
        rgb_bytes = bytes(barray)

        """ Create an RGB image from bytes """
        img = Image.frombytes('RGB', (width, height), rgb_bytes)

        img.save(output_image_path)

    except AssertionError as e:
        print(f"AssertionError: {e}")

    return barray
