from PIL import Image, ImageDraw, ImageFont


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
        font = ImageFont.truetype("arial.ttf", size=20)
        
        text = f"{text} - {author}"
        text_width, text_height = draw.textsize(text, font=font)
        x = (img.width - text_width) / 2
        y = img.height - text_height - 10

        draw.text((x, y), text, font=font, fill="white")

        output_path = f"{self.output_dir}/meme_{img_path.split('/')[-1]}"
        img.save(output_path)
        return output_path
