from PIL import Image
import numpy as np

def image_to_ascii(file_path, columns=80, scale=0.5, chars=" .,:;ox%#@"):
    """
    Converts an image to ASCII art

    Parameters
    ----------
    file_path : str
        Path to the image file
    columns : int, optional
        Number of columns in the ASCII art, by default 80
    scale : float, optional
        Scale factor for the image, by default 0.5
    chars : str, optional
        Characters to use in the ASCII art, by default " .,:;ox%#@"

    Returns
    -------
    str
        ASCII art
    
    The function works by resizing the image to the desired dimensions,
    and then converting it to grayscale. Then, the pixel values are
    mapped to ascii characters based on the pixel value range. The
    default characters are chosen such that they are ordered from
    darkest to lightest. ' ' is the darkest character
    and '@' is the lightest character. The characters are then
    concatenated row-wise to form the ASCII art.

    Note
    ----
    Black and white images with simple lines and shapes work best.
    The ASCII art may not be legible for complex images with many
    details. You can experiment with different parameters to get the
    best results for your image.

    You can modify the number of columns in the ASCII art. The
    default value of 80 works well for most images, but you can
    increase or decrease this value to change the width of the ASCII
    art. Increasing the number of columns will increase the width of
    the ASCII art, while decreasing the number of columns will
    decrease the width of the ASCII art. However, if you decrease the
    number of columns too much, the ASCII art may not be legible.

    You can also modify the scale factor to change the size of the
    ASCII art. For example, if you want the ASCII art to be twice the
    size of the original image, you can set scale to 1.0. If you want
    the ASCII art to be half the size of the original image, you can
    set scale to 0.5. You can also set scale to a value greater than
    1.0 to increase the size of the ASCII art beyond the size of the
    original image. However, this may result in a loss of quality.

    You can also modify the default characters to your liking. For example,
    if you want to use only 5 characters, you can set chars to
    '@%#*+' and the function will map the pixel values to these
    characters based on the pixel value range.
    """
    try:
        image = Image.open(file_path)

        width, height = image.size
        aspect_ratio = height / width
        new_width = columns
        new_height = int(scale * aspect_ratio * new_width)

        resized_image = image.resize((new_width, new_height))

        grayscale_image = resized_image.convert("L")

        pixel_values = np.array(grayscale_image)

        ascii_art = []

        pixel_range = 255 // len(chars)

        for row in pixel_values:
            row_chars = ""
            for pixel in row:
                index = pixel // pixel_range
                index = min(index, len(chars) - 1)
                row_chars += chars[index]
            ascii_art.append(row_chars)

        return "\n".join(ascii_art)
    except FileNotFoundError:
        return "Error: The file was not found. Check the file path."
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    image_path = 'img.png' # Replace with your image path

    ascii_art = image_to_ascii(image_path)

    if ascii_art.startswith("Error:"):
        print(ascii_art)
    else:
        with open('ascii_art.txt', 'w') as f: # Replace with your output file path, otherwise ascii_art.txt will be created
            f.write(ascii_art)