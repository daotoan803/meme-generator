import os
import random

import requests
from flask import Flask, render_template, request

from meme_engine.meme_engine import MemeEngine
from quote_engine.main_ingestor import Ingestor

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quote_list = []
    for file in quote_files:
        quote_list.extend(Ingestor.parse(file))

    images_path = "./_data/photos/dog/"
    images = []
    for img in os.listdir(images_path):
        if img.endswith(('jpg', 'png', 'jpeg')):
            images.append(os.path.join(images_path, img))

    return quote_list, images


quotes, imgs = setup()


def get_image(image_url: str):
    """
    Fetch an image from the given URL.
    Args:
        image_url (str): The URL of the image to download.

    Returns:
        requests.Response: The response object containing the image
        data if the request is successful.

    Raises:
        ValueError: If the URL is invalid, the request fails,
        or the response does not contain an image.
    """

    try:
        response = requests.get(image_url, timeout=10)
        if "image" not in response.headers["Content-Type"]:
            raise ValueError("The URL does not point to a valid image")
        return response
    except Exception as exc:
        raise ValueError('Image URL is invalid') from exc


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """
    try:
        image_url = request.form['image_url']
        body = request.form['body']
        author = request.form['author']

        # Download the image
        response = get_image(image_url)

        temp_img_path = './static/temp_image.jpg'
        with open(temp_img_path, 'wb') as file:
            file.write(response.content)

        # Generate the meme
        path = meme.make_meme(temp_img_path, body, author)

        # Remove the temporary image
        os.remove(temp_img_path)

        return render_template('meme.html', path=path)
    except ValueError as error:
        print(error)
        return render_template(
            'meme_form.html', error=error or 'Something went wrong')
    except Exception as error:
        print(error)
        return render_template('meme_form.html', error='Somethings went wrong')


if __name__ == "__main__":
    app.run()
