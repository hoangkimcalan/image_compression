from PIL import Image

image = Image.open('./input/input_4.jpg')

quality = 50

image.save('./output/output_5.jpg', optimize=True, quality=quality)
