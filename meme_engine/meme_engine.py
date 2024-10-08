import os

from PIL import Image, ImageDraw, ImageFont

FONT_PATH = os.path.join(
    os.path.dirname(__file__), "..", "assets", "arial.ttf")


class MemeEngine:
    """A class to generate memes by overlaying text on images.

    Attributes:
        output_dir (str): The directory where the generated memes will be
        saved.
    """

    def __init__(self, output_dir):
        """
        Initializes the MemeEngine with the output directory.

        Args:
            output_dir (str): The directory where the generated memes will be
            saved.
        """
        os.makedirs(output_dir, exist_ok=True)
        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500):
        """
        Creates a meme by adding a quote to an image and saves it.

        Args:
            img_path (str): The file path to the input image.
            text (str): The quote text to add to the image.
            author (str): The author of the quote.
            width (int, optional): The desired width of the meme. Defaults to
            500.

        Returns:
            str: The file path to the saved meme image.
        """
        img = Image.open(img_path)
        aspect_ratio = img.height / img.width
        new_height = int(width * aspect_ratio)
        img = img.resize((width, new_height), Image.Resampling.LANCZOS)

        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(FONT_PATH, size=20)
        text = f"{text} - {author}"
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        x = (img.width - text_width) / 2
        y = img.height - text_height - 10

        draw.text((x, y), text, font=font, fill="white")

        output_path = f"{self.output_dir}/meme_{img_path.split('/')[-1]}"
        img.save(output_path)
        return output_path
