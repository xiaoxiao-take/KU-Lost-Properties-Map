import openai
import os
from os.path import join, dirname
import base64
from dotenv import load_dotenv
import sys

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(verbose=True, dotenv_path=dotenv_path)

openai.api_key = os.getenv('OPEN_API_KEY')

NUMBER_OF_DUMMY_IMAGES = 4

def translate_ja_to_en(prompt):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": f"'{prompt}'を英訳してください。"},
    ],
    )
    return response.choices[0]["message"]["content"]

def generate_dummy_image(prompt):
    english_prompt = translate_ja_to_en(prompt)
    response = openai.Image.create(
        prompt=english_prompt,
        n=NUMBER_OF_DUMMY_IMAGES,
        size="512x512",
        response_format="b64_json",
    )
    dummy_images = []
    for data, n in zip(response["data"], range(NUMBER_OF_DUMMY_IMAGES)):
        dummy_image = base64.b64decode(data["b64_json"])
        # dummy_image = data["b64_json"]
        # with open(f"image_{n}.png", "wb") as f:
        #     f.write(dummy_image)
        dummy_images.append(dummy_image)
    return dummy_images

if __name__ == '__main__':
    prompt = sys.argv[1]
    generate_dummy_image(prompt)