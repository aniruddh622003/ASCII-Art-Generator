import PIL.Image as im

ASCII_Char = ['B', '@', '#', '$', 'U', '%', '?', '*', '+', '-', ';', '.']
# ASCII_Char = ['.', ';', '-', '+', '*', '?', '%', '$', '#', '@']
# ASCII_Char = ['B', '$', '@', '#', 'U', '%', '^', '*', '!', '.']


def resize(image, width=300):
    im_width, im_height = image.size
    ratio = (im_height/im_width)
    height = int(ratio * width * 0.55)
    resized_image = image.resize((width, height))
    return resized_image


def gray(image):
    gray_image = image.convert("L")
    return gray_image


def conversion_to_ascii(image):
    pixels = image.getdata()
    characters = "".join(ASCII_Char[pixel//24] for pixel in pixels)
    return characters


def main():
    path = input("Enter path to image: ")
    try:
        image = im.open(path)

    except:
        print(path, "is not a valid path to an image.")

    new_image_data = conversion_to_ascii(gray(resize(image)))
    pixel_count = len(new_image_data)
    ASCII_Image = "\n".join(new_image_data[i:(i+300)] for i in range(0, pixel_count, 300))

    print(ASCII_Image)

    with open("ascii_image.txt", "w") as f:
        f.write(ASCII_Image)


main()

