from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os


def generate_text(text: str, char_dict: dict, h_offset, v_offset):
    # Should be able to generate it raw left justified and execute command to center.. (in theory we could apply that)

    out = []

    pos_delta = [0, 0]

    for index, char in enumerate(text):
        if char == "\n":
            pos_delta = [0, pos_delta[1] + char_dict[" "]["h"] + v_offset]
            continue

        pos_delta = [pos_delta[0] + (char_dict[char]["w"] + h_offset) / 2.0, pos_delta[1]]

        char_out = {"type": "Sprite",
                    "filepath": char_dict[char]["path"],
                    "layer": "Foreground",
                    "position": pos_delta,
                    "tether": "Centre",
                    "index": index
                    "functions": []}

        pos_delta = [pos_delta[0] + (char_dict[char]["w"] + h_offset) / 2.0, pos_delta[1]]

        if char not in [" ", "\n"]:
            out.append(char_out)

    return out


def generate_image_files(font, size, out_path):
    # TODO Probably a good idea to programmatically allow or disallow blur and the like. Need to think about use case
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_\"'-,.?:;!&1234567890 "

    font = ImageFont.truetype(font, size)

    char_dict = {}

    path = os.path.dirname(__file__)[0:-5] + '/resources/fonts/'

    for ind, character in enumerate(characters):
        w = int(font.getlength(character))
        h = int(size * 1.25)

        char_dict[character] = {"w": w, "h": h, "path": '"' + out_path + str(ind) + '.png"'}

        const_adjust = 20

        # Add buffer room for blur
        img_w = w + const_adjust
        img_h = h + const_adjust

        image = Image.new(mode="RGBA", size=(img_w, img_h), color=(0, 0, 0, 0))
        draw = ImageDraw.Draw(image)

        draw.text(((img_w - w) / 2, (img_h - h) / 2), character, font=font, fill=(0, 0, 0, 255), align="center")

        # Do blurring
        image = image.filter(ImageFilter.GaussianBlur(7))
        draw = ImageDraw.Draw(image)
        draw.text(((img_w - w) / 2, (img_h - h) / 2), character, font=font, fill=(255, 255, 255, 255), align="center")

        out = "resources/" + out_path + str(ind) + ".png"

        image.save(out, format="PNG")

    return char_dict
