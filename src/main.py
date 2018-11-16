from PIL import Image
import os
import sys

dir = os.path.dirname(__file__)
img_path = os.path.join(dir, "img/img.jpg")

def hidden_keys(text):
	b_text_arr = [ord(t) for t in text]
	keys = []
	for uc in b_text_arr:
		for c in list(str(uc)):
			keys.append(int(c))

	return keys


def generate(text):
	keys = hidden_keys(text)
	img = Image.open(img_path)
	rgb_img = img.convert("RGB")
	img_size = rgb_img.size

	current = 0

	for x in range(img_size[0]):
		for y in range(img_size[1]):
			r, g, b = rgb_img.getpixel((x, y))
			print(bin(r))
			print(bin(g))
			print(bin(b))

	img.save(os.path.join(dir, "img/output.jpg"))

if __name__ == '__main__':
	args = sys.argv
	generate(args[1])
